import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.linspace(0., 10., 11)
y = 2.5 + 3.2 * x

def model(x, m, q):
    return m * x + q

popt, pcov = curve_fit(model, x, y)

plt.errorbar(x, y, fmt='o')
# Overlay the model without unpacking the best-fit parameters.
plt.plot(x, model(x, *popt))

# Compare with
# mhat, qhat = popt
# plt.plot(x, model(x, mhat, qhat))

