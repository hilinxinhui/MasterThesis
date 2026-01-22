import os
import glob
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='./id/MHSDT_Dmit_SL16_B2_T5/gts_mu_sigma_lower_upper.npz')
    parser.add_argument('-c', type=str, default='id')
    args = parser.parse_args()
    return args

def main(args):
    data = np.load(args.f)
    gts, mu, sigma = data['gts'], data['mu'], data['sigma']
    df = pd.DataFrame({'cycle index': range(1, len(gts) + 1), 'grounds truth': gts, 'preds': mu, 'uncertainty': 3*sigma})
    df.to_excel(os.path.join(args.c + '.xlsx'), index=None)

if __name__ == '__main__':
    args = get_config()
    main(args)
    