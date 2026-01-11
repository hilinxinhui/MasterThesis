import os
import json
import glob
import torch
import torch.nn as nn
from models.HSDT import StoTransformerEncoder, HSDTEncoder
from models.Regressor import Regressor
from datasets.mit_loader import MITDataset
from datasets.tri_loader import TRIDataset
from datasets.tongji_loader import TongjiDataset
from utils.utils import mkdir, save_to_txt

exps = [
    # "MHSDT_Dtri_SL16_B3_T1@2024-06-23_17-55-53",
    # "MHSDT_Dtri_SL16_B3_T2@2024-06-23_15-12-32",
    # "MHSDT_Dtri_SL16_B3_T3@2024-06-23_16-48-47",
    # "MHSDT_Dtri_SL16_B3_T4@2024-06-23_18-02-17",
    # "MHSDT_Dtri_SL16_B3_T6@2024-06-23_16-57-21",
    # "MHSDT_Dtri_SL16_B3_T7@2024-06-23_16-59-28",
    # "MHSDT_Dtri_SL16_B3_T8@2024-06-23_15-31-08",
    "MHSDT_Dtri_SL16_B3_T5@2024-06-18_19-28-21",
]

# done
exps_1 = [
    "MHSDT_Dmit_SL16_B2_T1@2024-06-23_16-34-46",
    "MHSDT_Dmit_SL16_B2_T2@2024-06-23_16-36-36",
    "MHSDT_Dmit_SL16_B2_T3@2024-06-23_16-38-20",
    "MHSDT_Dmit_SL16_B2_T4@2024-06-23_16-39-49",
    "MHSDT_Dmit_SL16_B2_T5@2024-06-23_15-08-02",
]


exps_3 = [
    "MHSDT_Dtongji_SL16_B2_T1@2024-06-22_22-54-31",
    "MHSDT_Dtongji_SL16_B2_T2@2024-06-18_19-33-00",
    "MHSDT_Dtongji_SL16_B2_T3@2024-06-22_22-56-56",
    "MHSDT_Dtongji_SL16_B2_T4@2024-06-22_22-58-07",
    "MHSDT_Dtongji_SL16_B2_T5@2024-06-18_23-22-15",
    "MHSDT_Dtongji_SL16_B2_T6@2024-06-20_08-28-20",
    "MHSDT_Dtongji_SL16_B2_T7@2024-06-19_23-22-18",
    "MHSDT_Dtongji_SL16_B2_T8@2024-06-20_08-30-00",
    "MHSDT_Dtongji_SL16_B2_T9@2024-06-18_23-25-36",
]


def get_config(path):
    res = os.listdir(path)
    assert "args_json.json" in res, f"No such file: args_json.json"
    with open(os.path.join(res_path, exp, "args_json.json"), "r") as f:
        config = json.load(f)
    return config


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
    # add_conv = config["add_conv"]
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


def calibrate(path, model):
    pass


if __name__ == "__main__":
    fake_input = torch.randn(111, 16, 192).to("cuda")
    res_path = "./best"
    assert os.path.exists(res_path), f"No such directory: {res_path}"
    for exp_id, exp in enumerate(exps):
        print(exp_id, exp)
        config = get_config(os.path.join(res_path, exp))
        print(config)
        model = get_model(os.path.join(res_path, exp), config)
        print(model(fake_input).shape)
        # break
