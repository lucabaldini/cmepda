class Line:
    """Class representing a straight line"""
    def __init__(self, slope=1., intercept=0.):
        self.slope = slope
        self.intercept = intercept
    
    def __call__(self, x):
        return self.slope * x + self.intercept
        
    def __str__(self):
        return 'y = {} x + {}'.format(self.slope, self.intercept)
    
    def __repr__(self):
        return 'Slope = {}, Intercept = {}'.format(self.slope, self.intercept)

line = Line(slope=-2., intercept=1.)
print(line)
print(repr(line))
print(line(2.))

