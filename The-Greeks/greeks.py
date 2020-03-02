import argparse
import numpy as np
import scipy.stats as ss
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
matplotlib.rcParams['text.usetex'] = True


# we assume that q=0


def interval_stock_price(args) -> float:
    S = np.linspace(args.S0, args.ST, 100)
    return S


def d1(args) -> float:
    d1 = (np.log(interval_stock_price(args) / args.E) + ((args.r / 100.0) + (args.sig / 100.0)**2 / 2) * (args.T / 365)) / ((args.sig / 100.0) * np.sqrt((args.T / 365)))
    return d1


def d2(args) -> float:
    d2 = (np.log(interval_stock_price(args) / args.E) + ((args.r / 100.0) - (args.sig / 100.0)**2 / 2) * (args.T / 364)) / ((args.sig / 100.0) * np.sqrt((args.T / 365)))
    return d2


def delta_ep(args) -> float:
    delta_ep = -1 * ss.norm.cdf(-1 * d1(args))
    return delta_ep


def delta_ec(args) -> float:
    delta_ec = ss.norm.cdf(d1(args))
    return delta_ec


def gamma(args) -> float:
    gamma = np.exp(-1 * 0.5 * d1(args) ** 2) / ((args.sig /100.0) * np.sqrt(2 * np.pi * (args.T / 365)) * interval_stock_price(args))
    return gamma


def rho_ec(args) -> float:
    rho_ec = (args.E * (args.T / 365) * np.exp((-args.r / 100.0) * (args.T / 365)) * ss.norm.cdf(d2(args))) / 100.0
    return rho_ec


def rho_ep(args) -> float:
    rho_ep = (-1 * args.E * (args.T / 365) * np.exp((-args.r / 100.0) * (args.T / 365)) * ss.norm.cdf(-1 * d2(args))) / 100.0
    return rho_ep


def vega(args) -> float:
    vega = (args.E * np.exp(-1 * (args.r / 100.0) * (args.T / 365)) * ss.norm.pdf(d2(args)) * np.sqrt((args.T / 365))) / 100
    return vega


def theta_ec(args) -> float:
    theta_ec = ((-1 * (args.sig / 100.0) * args.E * ss.norm.pdf(d2(args)) * np.exp((args.r / 100.0) * (args.T / 365))) / (2 * np.sqrt((args.T / 365))) \
                - np.exp((-args.r / 100.0) * (args.T / 365)) * (args.r / 100) * args.E * ss.norm.cdf(d2(args))) / 100.0
    return theta_ec


def theta_ep(args) -> float:
    theta_ep = ((-1 * (args.sig / 100.0) * args.E * ss.norm.pdf(d2(args)) * np.exp((args.r / 100.0) * (args.T / 365))) / (2 * np.sqrt((args.T / 365))) \
                + np.exp((-args.r / 100.0) * (args.T / 365)) * (args.r / 100) * args.E * ss.norm.cdf(d2(args))) / 100.0
    return theta_ep


def plot(args):
    if args.plot == 'delta':
        plt.subplot(2, 1, 1)
        plt.plot(interval_stock_price(args), delta_ec(args))
        plt.title("$\\Delta$ European Call")
        plt.xlabel("$S$")
        plt.ylabel("$\\Delta$")

        plt.subplot(2, 1, 2)
        plt.plot(interval_stock_price(args), delta_ep(args))
        plt.title("$\\Delta$ European Put")
        plt.xlabel("$S$")
        plt.ylabel("$\\Delta$")
        plt.tight_layout()
        plt.show()

    elif args.plot == 'gamma':
        plt.plot(interval_stock_price(args), gamma(args))
        plt.title("$\\Gamma$ European Option")
        plt.xlabel("$S$")
        plt.ylabel("$\\Gamma$")
        plt.show()

    elif args.plot == 'rho':
        plt.subplot(2, 1, 1)
        plt.plot(interval_stock_price(args), rho_ec(args))
        plt.title('$\\rho$ European Call')
        plt.xlabel("$S$")
        plt.ylabel("$\\rho$")

        plt.subplot(2, 1, 2)
        plt.plot(interval_stock_price(args), rho_ep(args))
        plt.title("$\\rho$ European Put")
        plt.xlabel("$S$")
        plt.ylabel("$\\rho$")
        plt.tight_layout()
        plt.show()

    elif args.plot == 'vega':
        plt.plot(interval_stock_price(args), vega(args))
        plt.title("$\\gamma$ European Option")
        plt.xlabel("$$")
        plt.ylabel("$\\gamma$")
        plt.show()

    elif args.plot == 'theta':
        plt.subplot(2, 1, 1)
        plt.plot(interval_stock_price(args), theta_ec(args))
        plt.title("$\\Theta$ European Call")
        plt.xlabel("$S$")
        plt.ylabel("$\\Theta$")

        plt.subplot(2, 1, 2)
        plt.plot(interval_stock_price(args), theta_ep(args))
        plt.title("$\\Theta$ European Put")
        plt.xlabel("$S$")
        plt.ylabel("$\\Theta$")
        plt.tight_layout()
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--S0', '-S0', type=float, default=0.0, help="Initial Stock Price")
    parser.add_argument('--ST', '-ST', type=float, default=0.0, help="Last Stock Price")
    parser.add_argument('--E', '-E', type=float, default=0.0, help="Exercise Price")
    parser.add_argument('--r', '-r', type=int, default=0, help="Interest Rate")
    parser.add_argument('--sig', '-sig', type=int, default=0, help="Sigma or Volatility")
    parser.add_argument('--T', '-T', type=int, default=0, help="Exercise Time (Interval Day)")
    parser.add_argument('--plot', '-plot', type=str, default='delta', help="What to Plot?")
    args = parser.parse_args()
    plot(args)


if __name__ == '__main__':
    main()
