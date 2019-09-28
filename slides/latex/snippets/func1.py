import math

def square(x):
    """Return the square of x.
    """
    return x * x

def cartesian_to_polar(x=1., y=1.):
    """Convert cartesian to polar coordinates.
    """
    r = math.sqrt(x**2. + y**2.)
    phi = math.atan2(y, x)
    return r, phi

print(square(2.))
print(cartesian_to_polar(0., 1.))
print(cartesian_to_polar())
