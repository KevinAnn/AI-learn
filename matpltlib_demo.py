import inline
import matplotlib

import matplotlib.pyplot as plt

import numpy as np

mu = 2
sigma = 0.5
v = np.random.normal(mu, sigma, 10000)

plt.hist(v, bins=50, density=1)
plt.show()