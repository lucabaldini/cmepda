import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline

x = np.linspace(0., 1., 10)
y = np.exp(3. * x) * np.sin(3. * x)

s1 = InterpolatedUnivariateSpline(x, y, k=1)
s3 = InterpolatedUnivariateSpline(x, y, k=3)

print(s1(0.234))
print(s1.integral(0.2, 0.8))
