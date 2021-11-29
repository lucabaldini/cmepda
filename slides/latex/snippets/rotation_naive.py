import numpy

def rotate(x, y, theta):
    """ Naive implementation. This works, but is inefficient - we have to
    calculate cos(theta) and sin(theta) for each pair (x,y)! """
    c = numpy.cos(theta)
    s = numpy.sin(theta)
    x_rot = c * x - s * y
    y_rot = s * x + c * y
    return x_rot, y_rot

x, y = 1., 0.
theta = numpy.pi/4
print(rotate(x, y, theta)) # Rotation of pi/2
    
def efficient_rotate(x, y, c_theta, s_theta):
    """ Efficient rotation. The user gives cos and sin, so they are not
    calculated for each pixel """
    x_rot = c * x - s * y
    y_rot = s * x + c * y
    return x_rot, y_rot
    
c = numpy.cos(theta)
s = numpy.sin(theta)
print(efficient_rotate(x, y, c, s)) # The syntax is very ugly!
