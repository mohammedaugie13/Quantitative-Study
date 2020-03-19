import numpy as np
import scipy as scp
import scipy.stats as ss
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from scipy.special import iv
from scipy.optimize import minimize

# np.random.seed(seed=42)
paths = 10
steps = 1000

# if mu equal to zero and sigma equal to one, is called Wiener porcess
mu = 0.2
sig = 0.312
T = 10
T_vec, dt = np.linspace(0, T, steps, retstep=True)


X0 = np.zeros((paths, 1))

#Brownian Increment
increments = ss.norm.rvs(loc=mu * dt, scale=np.sqrt(dt) * sig, size=(paths, steps - 1))
#Geometric Brownian Increment
increments_gbm = ss.norm.rvs(loc=(mu - 0.5 * sig ** 2)* dt, scale=np.sqrt(dt)*sig, size=(paths, steps - 1))
#Wiener Increment
increments_wiener = ss.norm.rvs(loc= 0 * dt, scale=np.sqrt(dt) * 1, size=(paths, steps - 1))


X = np.concatenate((X0, increments), axis=1).cumsum(1)
Y = np.concatenate((X0, increments_gbm), axis=1).cumsum(1)
Y_T = np.exp(Y)
W = np.concatenate((X0, increments_wiener), axis=1).cumsum(1)

plt.subplot(3, 1, 1)
plt.plot(T_vec, X.T)
plt.title("Brownian Paths")
plt.xlabel("T")

plt.subplot(3, 1, 2)
plt.plot(T_vec, Y_T.T)
plt.title(" Geometric Brownian Paths")
plt.xlabel("T")

plt.subplot(3, 1, 3)
plt.plot(T_vec, W.T)
plt.title(" Wiener Paths")
plt.xlabel("T")


plt.tight_layout()
plt.show()
