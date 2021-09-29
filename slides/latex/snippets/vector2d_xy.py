import math

class Vector2d:
    """ Class representing a Vector2d. We use float() to make sure of storing
    the coordinates in the correct format """   
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
   
    def module(self):
        return math.sqrt(self.x**2 + self.y**2)
       
    def angle(self):
        return math.atan2(self.y, self.x)
  
v = Vector2d(3., -1.)
print(v.x, v.y)
print(v.module(), v.angle())
