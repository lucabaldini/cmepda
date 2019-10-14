import numpy as np

a = np.linspace(0., 10., 11)
mask1 = a >= 2.5
mask2 = a < 8.5

print(a)
print(mask1)
print(mask2)
print(a[mask1])
print(a[mask2])
print(a[np.logical_and(mask1, mask2)])
