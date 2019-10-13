import random
import time
import numpy as np

# How many random numbers (uniformly distributed between 0 and 1) do you
# want to throw?
n = 1000000

# The slow way: explicit for loop in Python.
t0 = time.time()
x = []
for i in range(n):
    x.append(random.random())
dt = time.time() - t0
print('Elapsed time: %.3f s' % dt)

# The quick way: vectorizing in numpy
t0 = time.time()
x = np.random.random(size=n)
dt = time.time() - t0
print('Elapsed time: %.3f s' % dt)
