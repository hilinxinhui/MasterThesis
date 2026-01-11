import torch
import torch.nn as nn


class Regressor(nn.Module):
    def __init__(self, seq_len=16, emb_dim=16, dropout=0.1, out_dim=1, add_conv=False) -> None:
        super(Regressor, self).__init__()
        self.add_conv = add_conv
        # self.conv = nn.Conv1d(in_channels=16, out_channels=16, kernel_size=1)
        self.fc1 = nn.Linear(seq_len * emb_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, out_dim)
        self.relu1 = nn.ReLU()
        self.relu2 = nn.ReLU()
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)
        # self.regressor = nn.Sequential(
        #     nn.Linear(seq_len * emb_dim, 128),
        #     nn.ReLU(),
        #     nn.Dropout(dropout),
        #     nn.Linear(128, 64),
        #     nn.ReLU(),
        #     nn.Dropout(dropout),
        #     nn.Linear(64, out_dim),
        # )

    def forward(self, x):
        batch_size = x.shape[0]
        x = x.view(batch_size, -1)
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.dropout1(x)
        x = self.fc2(x)
        x = self.relu2(x)
        x = self.dropout2(x)
        x = self.fc3(x)
        return x
        # if self.add_conv:
        #     x = self.conv(x.permute(0, 2, 1))
        # out = self.regressor(x.view(x.size(0), -1))
        # return out


if __name__ == "__main__":
    from models.HSDT import HSDTEncoder

    # init device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"using device: {device}")

    # hyper parameters
    batch_size = 10
    seq_len = 16
    n_channel = 3
    resample_dim = 64
    input_dim = n_channel * resample_dim  # 192
    fea_dim = input_dim  # 192
    emb_dim = 16
    num_layers = 1
    heads = 2
    k_centroid = 2
    tau1 = 1.0
    tau2 = 1.0
    direction = 2
    dropout = 0.1
    forward_expansion = 1
    out_dim = 1

    # init model
    encoder = HSDTEncoder(
        fea_dim, emb_dim, num_layers, heads, k_centroid, tau1, tau2, direction, dropout, forward_expansion
    ).to(device)
    regressor = Regressor(seq_len, emb_dim, dropout, out_dim, add_conv=False).to(device)
    model = nn.Sequential(encoder, regressor).to(device)

    # fake input
    batch_x = torch.randn(batch_size, seq_len, input_dim).to(device)

    # single feed forward
    batch_y = model(batch_x)
    print(batch_y.shape)
