import numpy

def create_rotator(theta):
    """ Efficient rotation. Cosinus and sinus values are saved in the closure,
    so that they are computed exactly once."""
    c = numpy.cos(theta)
    s = numpy.sin(theta)
    def rotate(x, y):
        x_rot = c * x - s * y
        y_rot = s * x + c * y
        return x_rot, y_rot
    return rotate

x, y = 1., 0.
theta = numpy.pi/4
rotate_by_theta = create_rotator(theta)
print(rotate_by_theta(x, y))
