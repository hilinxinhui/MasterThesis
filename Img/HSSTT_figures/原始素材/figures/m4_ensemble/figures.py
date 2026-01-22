import os
import glob
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='./e1/Mensemble_Dtri_SL16_B3_T2/gts_mean_std_lower_upper.npz')
    parser.add_argument('-c', type=str, default='m4_tri_t2')
    args = parser.parse_args()
    return args

def main(args):
    data = np.load(args.f)
    gts, mu, sigma = data['gts'], data['mean'], data['std']
    df = pd.DataFrame({'cycle index': range(1, len(gts) + 1), 'grounds truth': gts, 'preds': mu, 'uncertainty': sigma})
    df.to_excel(os.path.join(args.c + '.xlsx'), index=None)

    plt.plot(gts)
    plt.plot(mu)
    plt.fill_between(range(len(mu)), mu - sigma, mu + sigma, alpha=0.4)
    plt.savefig(f'{args.c}.png')
    plt.close()

if __name__ == '__main__':
    args = get_config()
    main(args)
    