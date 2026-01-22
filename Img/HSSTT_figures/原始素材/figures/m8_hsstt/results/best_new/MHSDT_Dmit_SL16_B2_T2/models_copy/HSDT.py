import torch
import torch.nn as nn
import torch.nn.functional as F
from utils.utils import weight_reset


class StoSelfAttention(nn.Module):
    def __init__(self, hidden_dim, heads, tau):
        super(StoSelfAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.heads = heads
        self.head_dim = hidden_dim // heads
        self.tau = tau

        self.V_linear = nn.Linear(self.head_dim, self.head_dim)
        self.K_linear = nn.Linear(self.head_dim, self.head_dim)
        self.Q_linear = nn.Linear(self.head_dim, self.head_dim)
        self.FC_linear = nn.Linear(heads * self.head_dim, hidden_dim)

        self.reset_parameters()

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)

        # bacth_size, attention len, n_heads, head_dim
        Q = self.Q_linear(query.view(batch_size, -1, self.heads, self.head_dim))
        K = self.K_linear(key.view(batch_size, -1, self.heads, self.head_dim))
        V = self.V_linear(value.view(batch_size, -1, self.heads, self.head_dim))
        # print('Q, K, V', Q.size(), K.size(), V.size())

        key_out = torch.einsum("nqhd,nkhd->nhqk", [Q, K])  # batchx heads x query_len, key_len

        if mask is not None:
            key_out = key_out.masked_fill(mask == 0, float("-1e20"))

        # attention = torch.softmax(key_out / (self.hidden_dim ** (1 / 2)), dim=3)
        sto_attention = F.gumbel_softmax(key_out, tau=self.tau, hard=False, dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [sto_attention, V]).reshape(
            batch_size, query.shape[1], self.heads * self.head_dim
        )
        out = self.FC_linear(out)
        return out

    def reset_parameters(self):
        self.V_linear.reset_parameters()
        self.K_linear.reset_parameters()
        self.Q_linear.reset_parameters()
        self.FC_linear.reset_parameters()


class StoSelfDualAttention(nn.Module):
    def __init__(self, hidden_dim, heads, tau1, tau2, k_centroid, init_function=torch.nn.init.uniform_):
        super(StoSelfDualAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.heads = heads
        self.head_dim = hidden_dim // heads
        self.tau1 = tau1
        self.tau2 = tau2
        self.centroid = torch.nn.Parameter(
            init_function(torch.empty(self.head_dim, k_centroid), a=-0.5, b=0.5), requires_grad=True
        )

        self.V_linear = nn.Linear(self.head_dim, self.head_dim)
        self.K_linear = nn.Linear(self.head_dim, self.head_dim)
        self.Q_linear = nn.Linear(self.head_dim, self.head_dim)
        self.FC_linear = nn.Linear(heads * self.head_dim, hidden_dim)

        self.reset_parameters()

    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)

        # [batch_size, sentence_len, heads, heads_dim]
        Q = self.Q_linear(query.view(batch_size, -1, self.heads, self.head_dim))
        K = self.K_linear(key.view(batch_size, -1, self.heads, self.head_dim))
        V = self.V_linear(value.view(batch_size, -1, self.heads, self.head_dim))

        K_ = torch.einsum("nshd,dc->nshc", [K, self.centroid])
        prob = F.gumbel_softmax(K_, tau=self.tau1, hard=False, dim=-1)
        sto_K = torch.einsum("nshc,cd->nshd", [prob, self.centroid.T])
        key_out = torch.einsum("nqhd,nkhd->nhqk", [Q, sto_K])

        if mask is not None:
            key_out = key_out.masked_fill(mask == 0, float("-1e20"))

        sto_attention = F.gumbel_softmax(key_out, tau=self.tau2, hard=False, dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [sto_attention, V]).reshape(
            batch_size, query.shape[1], self.heads * self.head_dim
        )
        out = self.FC_linear(out)
        return out

    def reset_parameters(self):
        self.V_linear.reset_parameters()
        self.K_linear.reset_parameters()
        self.Q_linear.reset_parameters()
        self.FC_linear.reset_parameters()


# distance-sensitive attention module only
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


# stochastic distance-aware self attention
class SDAttention(nn.Module):
    def __init__(self, hidden_dim, heads, tau, seq_len=16, device="cuda"):
        super(StoSelfAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.heads = heads
        self.head_dim = hidden_dim // heads
        self.tau = tau
        self.seq_len = seq_len
        self.device = torch.device("cuda" if torch.cuda.is_available() and device == "cuda" else "cpu")

        self.V_linear = nn.Linear(self.head_dim, self.head_dim)
        self.K_linear = nn.Linear(self.head_dim, self.head_dim)
        self.Q_linear = nn.Linear(self.head_dim, self.head_dim)
        self.FC_linear = nn.Linear(heads * self.head_dim, hidden_dim)

        self.W = nn.Parameter(torch.ones(heads, 1, 1))
        self.V = nn.Parameter(torch.zeros(heads, 1, 1))

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

        # attention = torch.softmax(key_out / (self.hidden_dim ** (1 / 2)), dim=3)
        # sto_attention = F.gumbel_softmax(key_out, tau=self.tau, hard=False, dim=3)
        key_out = key_out * R.unsqueeze(0)
        sto_attention = F.gumbel_softmax(key_out, tau=self.tau, hard=False, dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [sto_attention, V]).reshape(
            batch_size, query.shape[1], self.heads * self.head_dim
        )
        out = self.FC_linear(out)
        return out

    def reset_parameters(self):
        self.V_linear.reset_parameters()
        self.K_linear.reset_parameters()
        self.Q_linear.reset_parameters()
        self.FC_linear.reset_parameters()


# hierarchical stochastic distance-aware self attention
class HSDAttention(nn.Module):
    def __init__(
        self,
        hidden_dim,
        heads,
        tau1,
        tau2,
        k_centroid,
        seq_len=16,
        device="cuda",
        init_function=torch.nn.init.uniform_,
    ):
        super(HSDAttention, self).__init__()
        self.hidden_dim = hidden_dim
        self.heads = heads
        self.head_dim = hidden_dim // heads
        self.tau1 = tau1
        self.tau2 = tau2
        self.centroid = torch.nn.Parameter(
            init_function(torch.empty(self.head_dim, k_centroid), a=-0.5, b=0.5), requires_grad=True
        )
        self.seq_len = seq_len
        self.device = torch.device("cuda" if torch.cuda.is_available() and device == "cuda" else "cpu")

        self.V_linear = nn.Linear(self.head_dim, self.head_dim)
        self.K_linear = nn.Linear(self.head_dim, self.head_dim)
        self.Q_linear = nn.Linear(self.head_dim, self.head_dim)
        self.FC_linear = nn.Linear(heads * self.head_dim, hidden_dim)

        self.W = nn.Parameter(torch.ones(heads, 1, 1))
        self.V = nn.Parameter(torch.zeros(heads, 1, 1))

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

        # [batch_size, sentence_len, heads, heads_dim]
        Q = self.Q_linear(query.view(batch_size, -1, self.heads, self.head_dim))
        K = self.K_linear(key.view(batch_size, -1, self.heads, self.head_dim))
        V = self.V_linear(value.view(batch_size, -1, self.heads, self.head_dim))

        K_ = torch.einsum("nshd,dc->nshc", [K, self.centroid])
        prob = F.gumbel_softmax(K_, tau=self.tau1, hard=False, dim=-1)
        sto_K = torch.einsum("nshc,cd->nshd", [prob, self.centroid.T])
        key_out = torch.einsum("nqhd,nkhd->nhqk", [Q, sto_K])

        if mask is not None:
            key_out = key_out.masked_fill(mask == 0, float("-1e20"))

        key_out = key_out * R.unsqueeze(0)
        sto_attention = F.gumbel_softmax(key_out, tau=self.tau2, hard=False, dim=3)
        out = torch.einsum("nhql,nlhd->nqhd", [sto_attention, V]).reshape(
            batch_size, query.shape[1], self.heads * self.head_dim
        )
        out = self.FC_linear(out)
        return out

    def reset_parameters(self):
        self.V_linear.reset_parameters()
        self.K_linear.reset_parameters()
        self.Q_linear.reset_parameters()
        self.FC_linear.reset_parameters()


class StoTransformerBlock(nn.Module):
    def __init__(
        self, emb_dim, heads, dropout, forward_expansion, k_centroid, tau1=1.0, tau2=1.0, direction=1
    ):
        super(StoTransformerBlock, self).__init__()

        if direction == 1:
            self.attention = StoSelfAttention(emb_dim, heads, tau2)
        elif direction == 2:
            self.attention = StoSelfDualAttention(emb_dim, heads, tau1, tau2, k_centroid)

        self.tau1 = tau1
        self.tau2 = tau2
        self.norm1 = nn.LayerNorm(emb_dim)
        self.norm2 = nn.LayerNorm(emb_dim)

        self.feed_forward = nn.Sequential(
            nn.Linear(emb_dim, forward_expansion * emb_dim),
            nn.ReLU(),
            nn.Linear(forward_expansion * emb_dim, emb_dim),
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, value, key, query, mask=None):

        attention = self.attention(query, key, value, mask)  # attention [batch_size, sentence_len, emb_dim]
        # tensor_l_k = torch.matmul(attention, self.centroid)        # tensor_l_k [batch_size, sentence_len, k_centroid] <= [batch_size, sentence_len, emb_dim] * [emb_dim, k_centroid]
        # option 1:
        # new_attention = torch.matmul(tensor_l_k, self.centroid.T)  # new_attention [batch_size, sentence_len, emb_dim] <= [batch_size, sentence_len, k_centroid] * [k_centroid, emb_dim]
        # option 2:
        # new_attention = torch.matmul(F.gumbel_softmax(tensor_l_k, tau=self.tau, hard=False), self.centroid.T)  # new_attention [batch_size, sentence_len, emb_dim] <= [batch_size, sentence_len, k_centroid] * [k_centroid, emb_dim]
        # Add skip connection, run through normalization and finally dropout
        x = self.dropout(self.norm1(attention + query))  # query [batch_size, sentence_len, emb_dim]
        forward = self.feed_forward(x)
        out = self.dropout(self.norm2(forward + x))
        return out

    def reset_parameters(self) -> None:
        self.attention.reset_parameters()
        self.feed_forward.apply(weight_reset)


class StoTransformerEncoder(nn.Module):

    def __init__(
        self,
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
        device="cuda",
    ):
        super(StoTransformerEncoder, self).__init__()
        self.emb_dim = emb_dim
        self.k_centroid = k_centroid
        self.device = device
        # sequence embedding
        self.seq_embedding = nn.Linear(fea_dim, emb_dim)  # [batch_size, 16, 192] -> [batch_size, 16, 512]
        # position embedding
        # self.position_embedding = nn.Embedding(max_len, emb_dim)

        self.layers = nn.ModuleList(
            [
                StoTransformerBlock(
                    emb_dim,
                    heads,
                    dropout=dropout,
                    forward_expansion=forward_expansion,
                    k_centroid=k_centroid,
                    tau1=tau1,
                    tau2=tau2,
                    direction=direction,
                )
                for _ in range(num_layers)
            ]
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None, emb=None):
        # print(f"shape of input: {x.shape}")
        batch_size, seq_len, fea_dim = x.shape
        # print(f"batch size: {batch_size}, sequence length: {seq_len}")
        # print(f"shape of sequence embedding: {self.seq_embedding(x).size()}")
        # positions = torch.arange(0, seq_len).expand(batch_size, seq_len).to(self.device)
        # print(f"shape of position embedding: {self.position_embedding(positions).size()}")
        sum_emb = self.seq_embedding(x)
        # sum_emb = self.seq_embedding(x) + self.position_embedding(positions)
        if emb is not None:
            sum_emb = sum_emb + emb
        out = self.dropout(sum_emb)

        for layer in self.layers:
            out = layer(out, out, out, mask)
        # print(f"shape of output of transformer encoder: {out.shape}")
        return out

    def reset_parameters(self) -> None:
        for layer in self.layers:
            layer.reset_parameters()


class HSDTBlock(nn.Module):
    def __init__(
        self, emb_dim, heads, dropout, forward_expansion, k_centroid, tau1=1.0, tau2=1.0, direction=1
    ):
        super(HSDTBlock, self).__init__()

        if direction == 1:
            self.attention = SDAttention(emb_dim, heads, tau2)
        elif direction == 2:
            self.attention = HSDAttention(emb_dim, heads, tau1, tau2, k_centroid)

        self.tau1 = tau1
        self.tau2 = tau2
        self.norm1 = nn.LayerNorm(emb_dim)
        self.norm2 = nn.LayerNorm(emb_dim)

        self.feed_forward = nn.Sequential(
            nn.Linear(emb_dim, forward_expansion * emb_dim),
            nn.ReLU(),
            nn.Linear(forward_expansion * emb_dim, emb_dim),
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, value, key, query, mask=None):

        attention = self.attention(query, key, value, mask)  # attention [batch_size, sentence_len, emb_dim]
        # tensor_l_k = torch.matmul(attention, self.centroid)        # tensor_l_k [batch_size, sentence_len, k_centroid] <= [batch_size, sentence_len, emb_dim] * [emb_dim, k_centroid]
        # option 1:
        # new_attention = torch.matmul(tensor_l_k, self.centroid.T)  # new_attention [batch_size, sentence_len, emb_dim] <= [batch_size, sentence_len, k_centroid] * [k_centroid, emb_dim]
        # option 2:
        # new_attention = torch.matmul(F.gumbel_softmax(tensor_l_k, tau=self.tau, hard=False), self.centroid.T)  # new_attention [batch_size, sentence_len, emb_dim] <= [batch_size, sentence_len, k_centroid] * [k_centroid, emb_dim]
        # Add skip connection, run through normalization and finally dropout
        x = self.dropout(self.norm1(attention + query))  # query [batch_size, sentence_len, emb_dim]
        forward = self.feed_forward(x)
        out = self.dropout(self.norm2(forward + x))
        return out

    def reset_parameters(self) -> None:
        self.attention.reset_parameters()
        self.feed_forward.apply(weight_reset)


class HSDTEncoder(nn.Module):
    def __init__(
        self,
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
        device="cuda",
    ):
        super(HSDTEncoder, self).__init__()
        self.emb_dim = emb_dim
        self.k_centroid = k_centroid
        self.device = device
        # sequence embedding
        self.seq_embedding = nn.Linear(fea_dim, emb_dim)  # [batch_size, 16, 192] -> [batch_size, 16, 512]

        self.layers = nn.ModuleList(
            [
                HSDTBlock(
                    emb_dim,
                    heads,
                    dropout=dropout,
                    forward_expansion=forward_expansion,
                    k_centroid=k_centroid,
                    tau1=tau1,
                    tau2=tau2,
                    direction=direction,
                )
                for _ in range(num_layers)
            ]
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None, emb=None):
        batch_size, seq_len, fea_dim = x.shape
        sum_emb = self.seq_embedding(x)
        if emb is not None:
            sum_emb = sum_emb + emb
        out = self.dropout(sum_emb)

        for layer in self.layers:
            out = layer(out, out, out, mask)
        return out

    def reset_parameters(self) -> None:
        for layer in self.layers:
            layer.reset_parameters()


if __name__ == "__main__":
    from models.Regressor import Regressor

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
    # encoder = StoTransformerEncoder(
    #     fea_dim, emb_dim, num_layers, heads, k_centroid, tau1, tau2, direction, dropout, forward_expansion
    # ).to(device)
    encoder = HSDTEncoder(
        fea_dim, emb_dim, num_layers, heads, k_centroid, tau1, tau2, direction, dropout, forward_expansion
    ).to(device)
    regressor = Regressor(seq_len, emb_dim, dropout, out_dim).to(device)
    model = nn.Sequential(encoder, regressor).to(device)
    print(model)

    # fake input
    batch_x = torch.randn(batch_size, seq_len, input_dim).to(device)

    # single feed forward
    batch_y = model(batch_x)
    print(batch_y.shape)
