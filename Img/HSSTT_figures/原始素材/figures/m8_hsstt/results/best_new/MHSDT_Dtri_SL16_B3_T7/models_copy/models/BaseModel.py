import os
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn

from models.Attention import Attention
from models.HSDT import HSDTEncoder, StoTransformerEncoder
from models.Regressor import Regressor
from utils.utils import AverageMeter
from utils.utils import mkdir, save_to_txt
from utils.utils import eval_metrix, get_nll, get_confidence_interval
from utils.torch_uncertainty.metrics.regression import MeanSquaredErrorInverse as iMSE
from utils.torch_uncertainty.metrics.regression import MeanAbsoluteErrorInverse as iMAE
from utils.torch_uncertainty.metrics.regression import MeanGTRelativeAbsoluteError as MAErel
from utils.torch_uncertainty.metrics.regression import MeanGTRelativeSquaredError as MSErel


class SOHMode(nn.Module):
    """
    data shape (N,16,192)
    """

    def __init__(self, args):
        super(SOHMode, self).__init__()
        self.args = args
        self.pre_net = self._preprocessing_net()
        self.backbone = self._backbone()
        self.pre_net.to(args.device)
        self.backbone.to(args.device)
        self._initialize_weights()
        self.optimizer = torch.optim.Adam(
            self.parameters(), lr=self.args.lr, weight_decay=self.args.weight_decay
        )
        if args.scheduler == "step":
            self.scheduler = torch.optim.lr_scheduler.StepLR(
                self.optimizer, step_size=args.lr_step, gamma=args.lr_gamma
            )
        elif args.scheduler == "multi_step":
            self.scheduler = torch.optim.lr_scheduler.MultiStepLR(
                self.optimizer,
                [30, 70],
                gamma=0.5,
            )

        self.mse = torch.nn.MSELoss()
        self.loss_meter = AverageMeter()
        self.best_state = None

    def _preprocessing_net(self):
        """
        A preprocess network which transform data from different sources into the same shape
        :return: A network, with output shape (b_s,n_channel,input_dim)
        """
        net = nn.Conv1d(in_channels=self.args.seq_len, out_channels=self.args.seq_len, kernel_size=1)
        return net

    def _backbone(self):
        fea_dim = self.args.fea_dim
        emb_dim = self.args.emb_dim
        num_layers = self.args.num_layers
        heads = self.args.heads
        k_centroid = self.args.k_centroid
        tau1 = self.args.tau1
        tau2 = self.args.tau2
        direction = self.args.direction
        dropout = self.args.dropout
        forward_expansion = self.args.forward_expansion
        out_dim = self.args.out_dim
        seq_len = self.args.seq_len
        device = torch.device(self.args.device)

        if self.args.model == "HSDT":
            encoder = HSDTEncoder(
                fea_dim,
                emb_dim,
                num_layers,
                heads,
                k_centroid,
                tau1,
                tau2,
                direction,
                dropout,
                forward_expansion,
                max_len=128,
                device=device,
            ).to(device)
            regressor = Regressor(seq_len, emb_dim, dropout, out_dim, add_conv=self.args.add_conv).to(device)
            backbone = nn.Sequential(encoder, regressor).to(device)
        elif self.args.model == "wo_d":
            assert direction == 2, f"wo_h model only support direction=2, but got {direction}"
            encoder = StoTransformerEncoder(
                fea_dim,
                emb_dim,
                num_layers,
                heads,
                k_centroid,
                tau1,
                tau2,
                direction,
                dropout,
                forward_expansion,
                max_len=128,
                device=device,
            ).to(device)
            regressor = Regressor(seq_len, emb_dim, dropout, out_dim).to(device)
            backbone = nn.Sequential(encoder, regressor).to(device)
        elif self.args.model == "wo_h":
            # wo_h & wo_d
            assert direction == 1, f"wo_h model only support direction=1, but got {direction}"
            encoder = StoTransformerEncoder(
                fea_dim,
                emb_dim,
                num_layers,
                heads,
                k_centroid,
                tau1,
                tau2,
                direction,
                dropout,
                forward_expansion,
                max_len=128,
                device=device,
            ).to(device)
            regressor = Regressor(seq_len, emb_dim, dropout, out_dim).to(device)
            backbone = nn.Sequential(encoder, regressor).to(device)
        elif self.args.model == "vanilla_trans":
            backbone = Attention()
        else:
            raise ValueError(f"model name {self.args.model} not invalid")

        return backbone

    def forward(self, x):
        if self.args.add_conv:
            x = self.pre_net(x)
            x = x.view(-1, self.args.seq_len, self.args.fea_dim)
        out = self.backbone(x)
        return out

    def _train_one_epoch(self, train_loader):
        self.pre_net.train()
        self.backbone.train()
        self.loss_meter.reset()
        for batch_idx, (batch_x, batch_y) in enumerate(train_loader):
            batch_x, batch_y = batch_x.to(self.args.device), batch_y.to(self.args.device)
            pred = self.forward(batch_x)
            loss = self.mse(pred.flatten(), batch_y.flatten())

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            self.loss_meter.update(loss.item())

    def predict(self, test_loader):
        # self.pre_net.eval()
        # self.backbone.eval()
        self.loss_meter.reset()
        with torch.no_grad():
            true_label = []
            pred_label = []
            for batch_idx, (batch_x, batch_y) in enumerate(test_loader):
                batch_x, batch_y = batch_x.to(self.args.device), batch_y.to(self.args.device)
                pred = self.forward(batch_x)
                loss = self.mse(pred.flatten(), batch_y.flatten())

                self.loss_meter.update(loss.item())
                true_label.append(batch_y.cpu().detach().numpy())
                pred_label.append(pred.cpu().detach().numpy())
            true_label = np.concatenate(true_label)
            pred_label = np.concatenate(pred_label)
        return true_label, pred_label

    def infer(self, test_loader):
        gts, pred_lts = [], []
        with torch.no_grad():
            for batch_idx, (batch_x, batch_y) in enumerate(test_loader):
                batch_x, batch_y = batch_x.to(self.args.device), batch_y.to(self.args.device)
                pred_lts.append(
                    [self.forward(batch_x).squeeze().cpu().numpy() for _ in range(self.args.n_sample)]
                )
                gts.extend(batch_y.cpu().numpy())

        gts = np.array(gts).flatten()
        pred_lst = np.array(pred_lts)
        pred_mean = np.mean(pred_lst, axis=1)
        pred_std = np.std(pred_lst, axis=1)
        lower = pred_mean - 3 * pred_std
        upper = pred_mean + 3 * pred_std

        plot_index = np.array(range(1, len(gts) + 1))

        # I qualitative results
        ## v1
        plt.plot(gts, label="gt")
        plt.errorbar(plot_index, pred_mean, yerr=3 * pred_std, label="pred")
        plt.xlabel("cycle")
        plt.ylabel("normalized state-of-health")
        plt.legend()
        plt.savefig(os.path.join(self.args.save_dir, "res_v1.png"))
        plt.close()
        ## v2
        plt.plot(pred_mean, label="pred")
        plt.fill_between(plot_index, lower, upper, alpha=0.5, label="uncertainty")
        plt.plot(gts, label="gt")
        plt.xlabel("cycle")
        plt.ylabel("normalized state-of-health")
        plt.legend()
        plt.savefig(os.path.join(self.args.save_dir, "res_v2.png"))
        plt.close()

        # II calibration results
        exp_CI, model_CI, ece = get_confidence_interval(gts, pred_mean, 3 * pred_std)
        plt.plot(exp_CI, model_CI, color="blue", label="observed")
        plt.plot([0, 100], [0, 100], color="black", linestyle="dashed", label="ideal")
        plt.xlabel("Expected Confidence")
        plt.ylabel("Precited Confidence")
        plt.legend()
        plt.savefig(os.path.join(self.args.save_dir, "calibration.png"))
        plt.close()

        # III model
        if self.args.is_save_best_model:
            model_path = os.path.join(self.args.save_dir, "best_model.pkl")
            torch.save(self.best_state, model_path)

        # IV qualitative results
        res_path = os.path.join(self.args.save_dir, "gts_mu_sigma_lower_upper.npz")
        np.savez(res_path, gts=gts, mu=pred_mean, sigma=pred_std, lower=lower, upper=upper)
        res_path = os.path.join(self.args.save_dir, "exp_obs.npz")
        np.savez(res_path, exp=exp_CI, obs=model_CI)

        # V metrics
        ## mae, rmse, nll, ece
        eval_imae = iMAE()
        eval_imse = iMSE()
        eval_mae_rel = MAErel()
        eval_mse_rel = MSErel()
        mae, mape, mse, rmse = eval_metrix(gts, pred_mean)
        nll = get_nll(gts, pred_mean, pred_std)
        imae = eval_imae(torch.tensor(gts).float(), torch.tensor(pred_mean).float())
        imse = eval_imse(torch.tensor(gts).float(), torch.tensor(pred_mean).float())
        mae_rel = eval_mae_rel(torch.tensor(gts).float(), torch.tensor(pred_mean).float())
        mse_rel = eval_mse_rel(torch.tensor(gts).float(), torch.tensor(pred_mean).float())
        res_string = f"mae: {mae}\nmape: {mape}\nmse: {mse}\nrmse: {rmse}\nnll: {nll}\nece: {ece}\nimae: {imae}\nimse: {imse}\nmae_rel: {mae_rel}\nmse_rel: {mse_rel}"
        save_to_txt(os.path.join(self.args.save_dir, "res.txt"), res_string)

    def Train(self, train_loader, valid_loader, test_loader, save_folder=None):
        min_loss = 1e3
        stop = 0
        self.train_loss = []
        self.valid_loss = []
        self.true_label, self.pred_label = None, None

        for e in range(1, self.args.n_epoch + 1):
            self._train_one_epoch(train_loader)
            self.scheduler.step()
            train_l = self.loss_meter.avg
            self.train_loss.append(train_l)
            stop += 1

            self.predict(test_loader)
            valid_l = self.loss_meter.avg
            self.valid_loss.append(valid_l)

            lr = self.optimizer.state_dict()["param_groups"][0]["lr"]
            print(
                f"\r epoch=[{e}/{self.args.n_epoch}]  train loss : {train_l:.5f}  valid loss : {valid_l:.5f}  lr : {lr:.5f} ",
                end="",
            )
            if e % 10 == 0:
                print("")

            if valid_l < min_loss:
                self.best_state = {
                    "pre_net": self.pre_net.state_dict(),
                    "backbone": self.backbone.state_dict(),
                }
                self.true_label, self.pred_label = self.predict(valid_loader)
                print(f" ------ test loss : {self.loss_meter.avg:.5f}")
                min_loss = valid_l
                stop = 0
            if stop >= self.args.early_stop:
                print("early stop!")
                break
        if save_folder is not None:
            self.infer(test_loader)

    # def save_all(self, folder):
    #     if not os.path.exists(folder):
    #         os.makedirs(folder)

    #     # prefix = self.args.model + "_" + self.args.input_type
    #     errors = eval_metrix(self.true_label, self.pred_label)
    #     np.savez(
    #         os.path.join(folder, f"TrainLoss_ValidLoss_TrueLabel_PredLabel_Errors.npz"),
    #         train_loss=np.array(self.train_loss),
    #         valid_loss=np.array(self.valid_loss),
    #         true_label=np.array(self.true_label),
    #         pred_label=np.array(self.pred_label),
    #         test_errors=np.array(errors),
    #     )
    #     torch.save(self.best_state, os.path.join(folder, "model.pkl"))
    #     plt.plot(self.true_label, label="gts")
    #     plt.plot(self.pred_label, label="preds")
    #     plt.savefig(os.path.join(folder, f"res.png"))
    #     plt.close()

    # def _plot_loss(self, train_loss, valid_loss):

    #     self.fig_loss = plt.figure()
    #     plt.plot(train_loss, label="train")
    #     plt.plot(valid_loss, label="valid")
    #     plt.xlabel("epoch")
    #     plt.ylabel("MSE")
    #     plt.legend()
    #     plt.show()
    #     plt.close()

    # def _plot_pred(self, true_label, pred_label):
    #     self.fig_pred = plt.figure()
    #     plt.plot(true_label, label="true")
    #     plt.plot(pred_label, label="pred")
    #     plt.xlabel("sample")
    #     plt.ylabel("SOH")
    #     plt.legend()
    #     plt.show()
    #     plt.close()

    def _initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv1d):
                nn.init.kaiming_normal_(m.weight, mode="fan_out", nonlinearity="relu")
                if m.bias is not None:
                    nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.BatchNorm1d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                nn.init.constant_(m.bias, 0)


if __name__ == "__main__":
    from main import get_config

    args = get_config()
    model = SOHMode(args)

    x1 = torch.rand(30, 16, 192).to("cuda")
    # x2 = torch.rand(30, 1, 67)

    y = model(x1)
    print(model)
    print("output shape:", y.shape)
