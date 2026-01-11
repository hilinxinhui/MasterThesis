import torch
import torch.nn as nn
import torch.nn.functional as F


def weight_reset(m):
    if isinstance(m, nn.Conv2d) or isinstance(m, nn.Linear):
        m.reset_parameters()


class DistanceSensitiveSelfAttention(nn.Module):
    def __init__(self, hidden_dim, heads, device, seq_len=16):
        super(DistanceSensitiveSelfAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.heads = heads
        self.head_dim = hidden_dim // heads
        self.seq_len = seq_len

        self.Q_linear = nn.Linear(self.head_dim, self.head_dim)
        self.K_linear = nn.Linear(self.head_dim, self.head_dim)
        self.V_linear = nn.Linear(self.head_dim, self.head_dim)
        self.FC_linear = nn.Linear(heads * self.head_dim, hidden_dim)

        self.W = nn.Parameter(torch.ones(heads, 1, 1))
        self.V = nn.Parameter(torch.zeros(heads, 1, 1))

        self.device = device

        self.reset_parameters()

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)

        # distance
        i, j = torch.meshgrid(torch.arange(1), torch.arange(self.seq_len), indexing="ij")
        indexes = torch.stack([i.flatten(), j.flatten()]).to(self.device)
        R = torch.abs(indexes.transpose(0, 1).unsqueeze(-1) - indexes.unsqueeze(0)).sum(1)
        R = self.W * R.unsqueeze(0)
        V_ = self.V.expand_as(R)
        R = torch.div(1 + torch.exp(V_), 1 + torch.exp(V_ - R))

        # bacth_size, attention len, n_heads, head_dim
        Q = self.Q_linear(query.view(batch_size, -1, self.heads, self.head_dim))
        K = self.K_linear(key.view(batch_size, -1, self.heads, self.head_dim))
        V = self.V_linear(value.view(batch_size, -1, self.heads, self.head_dim))
        # print('Q, K, V', Q.size(), K.size(), V.size())

        key_out = torch.einsum("nqhd,nkhd->nhqk", [Q, K])  # batchx heads x query_len, key_len

        if mask is not None:
            key_out = key_out.masked_fill(mask == 0, float("-1e20"))

        attention = torch.softmax(key_out * R.unsqueeze(0) / (self.hidden_dim ** (1 / 2)), dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [attention, V]).reshape(
            batch_size, query.shape[1], self.heads * self.head_dim
        )
        out = self.FC_linear(out)
        return out

    def reset_parameters(self):
        self.V_linear.reset_parameters()
        self.K_linear.reset_parameters()
        self.Q_linear.reset_parameters()
        self.FC_linear.reset_parameters()


class DistanceSensitiveAttentionBlock(nn.Module):
    def __init__(self, emb_dim, heads, droupout, forward_expansion, device):
        super(DistanceSensitiveAttentionBlock, self).__init__()
        self.attention = DistanceSensitiveSelfAttention(emb_dim, heads, device)
        self.norm1 = nn.LayerNorm(emb_dim)
        self.norm2 = nn.LayerNorm(emb_dim)
        self.feed_forward = nn.Sequential(
            nn.Linear(emb_dim, forward_expansion * emb_dim),
            nn.ReLU(),
            nn.Linear(forward_expansion * emb_dim, emb_dim),
        )
        self.dropout = nn.Dropout(droupout)
        self.device = device
        self.reset_parameters()

    def forward(self, key, value, query, mask=None):
        attention = self.attention(query, key, value, mask)
        x = self.dropout(self.norm1(attention + query))
        forward = self.feed_forward(x)
        out = self.dropout(self.norm2(x + forward))
        return out

    def reset_parameters(self) -> None:
        self.attention.reset_parameters()
        self.feed_forward.apply(weight_reset)


class DistanceSensitiveTransformerEncoder(nn.Module):
    def __init__(self, fea_dim, emb_dim, num_layers, heads, dropout=0.1, forward_expansion=2, device="cpu"):
        super(DistanceSensitiveTransformerEncoder, self).__init__()
        self.emb_dim = emb_dim
        self.seq_embedding = nn.Linear(fea_dim, emb_dim)
        self.position_embedding = nn.Embedding(512, emb_dim)
        self.layers = nn.ModuleList(
            [
                DistanceSensitiveAttentionBlock(emb_dim, heads, dropout, forward_expansion, device)
                for _ in range(num_layers)
            ]
        )
        self.dropout = nn.Dropout(dropout)
        self.device = device

        self.reset_parameters()

    def forward(self, x, mask=None, emb=None):
        batch_size, seq_len, fea_dim = x.shape
        positions = torch.arange(0, seq_len).expand(batch_size, seq_len).to(self.device)
        # sum_emb = self.seq_embedding(x) + self.position_embedding(positions)
        sum_emb = self.seq_embedding(x)
        if emb is not None:
            sum_emb += emb
        out = self.dropout(sum_emb)
        for layer in self.layers:
            out = layer(out, out, out, mask)

        return out

    # def reset_parameters(self):
    #     for layer in self.layers:
    #         layer.reset_parameters()


# class Regressor(nn.Module):
#     def __init__(self, seq_len, emb_dim, out_dim, dropout=0.1) -> None:
#         super(Regressor, self).__init__()
#         self.fc1 = nn.Linear(seq_len * emb_dim, 128)
#         self.fc2 = nn.Linear(128, 64)
#         self.fc3 = nn.Linear(64, out_dim)
#         self.relu1 = nn.ReLU()
#         self.relu2 = nn.ReLU()
#         self.dropout1 = nn.Dropout(dropout)
#         self.dropout2 = nn.Dropout(dropout)

#     def forward(self, x):
#         batch_size = x.shape[0]
#         x = x.view(batch_size, -1)
#         x = self.fc1(x)
#         x = self.dropout1(x)
#         x = self.relu1(x)
#         x = self.fc2(x)
#         x = self.dropout2(x)
#         x = self.relu2(x)
#         x = self.fc3(x)

#         return x


if __name__ == "__main__":
    from models.Regressor import Regressor

    # parameters and hyperparameters
    batch_size = 32
    fea_dim = 192
    # fea_dim = 128
    emb_dim = 256
    num_layers = 2
    heads = 2
    dropout = 0.1
    forward_expansion = 2
    seq_len = 16
    # input_channel = 24
    out_dim = 1  # regression task
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"using device: {device}")

    # input
    input = torch.rand(batch_size, seq_len, fea_dim).to(device)
    print(input.shape)

    # model
    encoder = DistanceSensitiveTransformerEncoder(
        fea_dim, emb_dim, num_layers, heads, dropout, forward_expansion, device
    ).to(device)
    regressor = Regressor(seq_len, emb_dim, out_dim, dropout).to(device)
    model = nn.Sequential(encoder, regressor).to(device)
    print(next(model.parameters()).device)

    # forward
    print(model(input).shape)
