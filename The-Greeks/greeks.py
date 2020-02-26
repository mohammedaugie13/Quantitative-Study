import argparse
import numpy as np
import scipy as scp
import scipy.stats as ss
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



#we assume that q=0


def interval_stock_price(args):
    S = np.linspace(args.S0, args.ST, 100)
    return S

def d1(args):
    d1 = (np.log(interval_stock_price(args)/args.E) + (args.r + args.sig**2 / 2) * args.T) / (args.sig * np.sqrt(args.T))
    return d1


def d2(args):
    d2 = (np.log(interval_stock_price(args)/args.E) + (args.r - args.sig**2 / 2) * args.T) / (args.sig * np.sqrt(args.T))
    return d2

def delta_ep(args):
    delta_ep = -1 * ss.norm.cdf(-1* d1(args))
    return delta_ep

def delta_ec(args):
    delta_ec = ss.norm.cdf(d1(args))
    return delta_ec

def plot(args):
    plt.subplot(2, 1, 1)
    plt.plot(interval_stock_price(args), delta_ec(args))
    plt.title("Delta European Call")
    plt.xlabel("S")
    plt.ylabel("Delta")

    plt.subplot(2, 1, 2)
    plt.plot(interval_stock_price(args), delta_ep(args))
    plt.title("Delta European Put")
    plt.xlabel("S")
    plt.ylabel("Delta")
    plt.tight_layout()
    plt.show()





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--S0','-S0', type=float, default=0.0, help="Initial Stock Price")
    parser.add_argument('--ST','-ST', type=float, default=0.0, help="Last Stock Price")
    parser.add_argument('--E','-E', type=float, default=0.0, help="Exercise Price")
    parser.add_argument('--r','-r', type=float, default=0.0, help="Interest Rate")
    parser.add_argument('--sig','-sig', type=float, default=0.0, help="Sigma or Drift Constant")
    parser.add_argument('--T','-T', type=float, default=0.0, help="Exercise Time (Interval Day per 365)")
    args = parser.parse_args()
    plot(args)


if __name__ == '__main__':
    main()
