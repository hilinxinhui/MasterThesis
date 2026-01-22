import torch
import torch.nn as nn


class Attention(nn.Module):
    """
    # input shape: (N,3,128)
    input shape: (N,16,192)
    """

    def __init__(self, dmodel=128):
        super(Attention, self).__init__()
        self.dmodel = dmodel
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=self.dmodel, nhead=4, dim_feedforward=128)
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer=self.encoder_layer, num_layers=2, enable_nested_tensor=False
        )
        self.linear = nn.Linear(16, self.dmodel)
        self.conv = nn.Conv1d(in_channels=self.dmodel, out_channels=8, kernel_size=1)
        self.predictor = nn.Sequential(nn.Linear(192 * 8, 64), nn.ReLU(), nn.Linear(64, 1))

    def forward(self, x):
        """
        :param x: (N,16,192)  (N,C,L)
        :return:
        """
        x = x.transpose(1, 2)  # (N,L,C)
        x = self.linear(x)  # (N, 192, 16) -> (N, 192, 128)
        out = self.transformer_encoder(x)  # (N,L,d_model)
        fea = self.conv(out.transpose(1, 2))  # (N,d_model,L) -> (N,8,L)
        pred = self.predictor(fea.view(fea.shape[0], -1))
        return pred


if __name__ == "__main__":
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

    # init model
    model = Attention().to(device)
    print(model)
    # num_params = sum(param.numel() for param in net.parameters())
    # print(f'number of parameters: {num_params}')

    # fake input
    batch_x = torch.rand((10, 16, 192)).to(device)  # (batch_size, seq_len, input_dim)

    # single feed forward
    batch_y = model(batch_x)
    print(batch_y.shape)
