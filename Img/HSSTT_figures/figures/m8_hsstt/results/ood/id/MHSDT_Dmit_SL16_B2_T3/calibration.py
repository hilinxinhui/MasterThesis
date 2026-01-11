# cd path/to/this/repo
# export PYTHONPATH=$(pwd)
import os
import json
import argparse
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from models_copy.HSDT import StoTransformerEncoder, HSDTEncoder
from models_copy.Regressor import Regressor
from datasets.mit_loader import MITDataset
from utils.utils import mkdir, save_to_txt
from utils.calibrated_regression import CalibratedRegression


np.random.seed(0)


def posterior_predictive(path, config):
    res = os.listdir(path)
    assert "gts_mu_sigma_lower_upper.npz" in res, f"No such file: gts_mu_sigma_lower_upper.npz"
    data = np.load(os.path.join(path, "gts_mu_sigma_lower_upper.npz"))
    gts, mu, sigma, lower, upper = data["gts"], data["mu"], data["sigma"], data["lower"], data["upper"]
    samples = np.random.normal(mu, sigma * 2.5, size=(config["n_sample"], len(gts)))
    return samples.T


def get_config(path):
    res = os.listdir(path)
    assert "args_json.json" in res, f"No such file: args_json.json"
    with open(os.path.join("./" "args_json.json"), "r") as f:
        config = json.load(f)
    return config


def get_data(config):
    assert config["data"] == "mit", f"dataset mismatch"
    config["data_root_dir"] = "../../../data"
    config = argparse.Namespace(**config)
    data_module = MITDataset(config)
    data_dict = data_module.get_charge()
    train_set, valid_set, test_set = data_dict["train"], data_dict["valid"], data_dict["test"]
    return train_set, valid_set, test_set


def get_model(path, config):
    fea_dim = config["fea_dim"]
    emb_dim = config["emb_dim"]
    num_layers = config["num_layers"]
    heads = config["heads"]
    k_centroid = config["k_centroid"]
    tau1 = config["tau1"]
    tau2 = config["tau2"]
    direction = config["direction"]
    dropout = config["dropout"]
    forward_expansion = config["forward_expansion"]
    out_dim = config["out_dim"]
    seq_len = config["seq_len"]
    add_conv = config["add_conv"]
    device = torch.device(config["device"])

    res = os.listdir(path)
    print(path)
    print(res)
    if "model.pth" in res:
        # without pre_net
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
        model = nn.Sequential(encoder, regressor).to(device)
        model_ckpt = torch.load(os.path.join(path, "model.pth"))
        model.load_state_dict(model_ckpt)
    elif "best_model.pkl" in res:
        # with prenet
        pre_net = nn.Conv1d(in_channels=16, out_channels=16, kernel_size=1).to(device)
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
        regressor = Regressor(seq_len, emb_dim, dropout, out_dim).to(device)
        backbone = nn.Sequential(encoder, regressor)
        pre_net_ckpt = torch.load(os.path.join(path, "best_model.pkl"))["pre_net"]
        backbone_ckpt = torch.load(os.path.join(path, "best_model.pkl"))["backbone"]
        pre_net.load_state_dict(pre_net_ckpt)
        backbone.load_state_dict(backbone_ckpt)
        model = nn.Sequential(pre_net, backbone)
    return model


def calibrate(X, y, model, path, config):
    calib = CalibratedRegression(X, y, model, pp=posterior_predictive, path=path, config=config).fit()
    fig, ax = plt.subplots(nrows=1, ncols=1)
    calib.plot_calibration_curve(ax)
    exp_ci, pred_ci = calib.predicted_cdf * 100, calib.empirical_cdf * 100
    ece = np.mean(np.abs(exp_ci - pred_ci))
    plt.plot(exp_ci, pred_ci, color="blue", label="observed")
    plt.plot([0, 100], [0, 100], color="black", linestyle="dashed", label="ideal")
    plt.xlabel("Expected Confidence")
    plt.ylabel("Precited Confidence")
    plt.legend()
    plt.savefig("after_calibration.png")
    plt.close()

    return exp_ci, pred_ci, ece


def update_results(path, res):
    exp_ci = res["exp_ci"]
    pred_ci = res["pred_ci"]
    ece = res["ece"]
    res_path = os.path.join(path, "res.txt")
    assert os.path.exists(res_path), f"No such file: res.txt"
    with open(res_path, "a") as f:
        f.write(f"ece_after_recalibration: {ece}\n")
    res_path = os.path.join(path, "exp_obs_re.npz")
    np.savez(res_path, exp=exp_ci, obs=pred_ci)


if __name__ == "__main__":
    cwd = os.getcwd()
    config = get_config(cwd)
    model = get_model(cwd, config)
    train_set, valid_set, test_set = get_data(config)
    X_train, y_train = train_set[:][0].numpy(), train_set[:][1].numpy()
    X_valid, y_valid = valid_set[:][0].numpy(), valid_set[:][1].numpy()
    X_test, y_test = test_set[:][0].numpy(), test_set[:][1].numpy()

    exp_ci, pred_ci, ece = calibrate(X_test, y_test, model, cwd, config)
    # print(ece)
    update_results(cwd, {"exp_ci": exp_ci, "pred_ci": pred_ci, "ece": ece})

    del X_train, y_train
    del X_valid, y_valid
    del X_test, y_test
    del model
