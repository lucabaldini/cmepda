import numpy as np

# arrays and lists seem similar...
l = [1., 2., 3.]
a = np.array(l)
print(l)
print(a)

# ...but they support basic arithmetic in a different fashion
print(l + l)
print(a + a)
