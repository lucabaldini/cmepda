import math

class Vector2d:
    """ Class representing a Vector2d. We use float() to make sure of storing
    the coordinates in the correct format """   
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
   
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)
       
    def info(self):
        print ('Vector2d({}, {})'.format(self.x, self.y))
         
    def add(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
       
v = Vector2d(3., -1.)
v.info()
print(v.module())
z = Vector2d(1., 1.5)
t = v.add(z)
t.info()
