import numpy as np
from matplotlib import pyplot as plt

x = np.logspace(0.2, 7, 500)

plt.figure('bigo')
plt.plot(x, np.log10(x), label='O(log(n))')
plt.plot(x, x, label='O(n)')
plt.plot(x, x * np.log10(x), label='O(nlog(n))')
plt.plot(x, x**2, label='O(n$^2$)')
plt.xlabel('n')
plt.ylabel('f(n)')
plt.xscale('log')
plt.yscale('log')
plt.grid(which='both', color='lightgray', ls='dashed')
plt.legend()
plt.show()
