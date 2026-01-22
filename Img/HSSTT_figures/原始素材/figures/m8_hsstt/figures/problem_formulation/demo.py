import os
import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt

res_path = '../../results/best_new/MHSDT_Dmit_SL16_B2_T2/gts_mu_sigma_lower_upper.npz'
bbb_res_path = '../../results/bbb_gts_mean_std_lower_upper.npz'

data = np.load(res_path)
bbb_data = np.load(bbb_res_path)
gts, mu, sigma, lower, upper = data['gts'], data['mu'], data['sigma'], data['lower'], data['upper']
# print(gts.shape, mu.shape)
blind_mu = bbb_data['mean']
hall_mu = mu + random.normal(loc=0.1, scale=0.02, size=(663,))
hall_sigma = sigma + random.normal(loc=0, scale=0.01, size=(663,))

fig, ax = plt.subplots(1, 3, figsize=(18, 4))

# Blind
ax[0].plot(gts)
ax[0].plot(blind_mu)

# Hallucinational
ax[1].plot(gts)
ax[1].plot(hall_mu)
ax[1].fill_between(range(1, 1 + len(gts)), hall_mu - 2 * hall_sigma, hall_mu + 2 * hall_sigma, alpha=0.5)

# Trustworthy
ax[2].plot(gts)
ax[2].plot(mu)
ax[2].fill_between(range(1, 1 + len(gts)), lower, upper, alpha=0.5)

plt.tight_layout()
plt.savefig('demo.png')

df = pd.DataFrame({
    'index': np.array(range(1, 1+len(gts))),
    'gts': gts,
    'blind': blind_mu,
    'hallucinational_mu': hall_mu,
    'hallucinational_sigma': 2 * hall_sigma,
    'trustworthy_mu': mu,
    'trustworthy_sigma': 3 * sigma 
})

df.to_excel('problem.xlsx', index=False)