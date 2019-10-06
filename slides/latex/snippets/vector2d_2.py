import math

class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
    def __abs__(self):
        # Special method!
        return math.sqrt(self.x**2 + self.y**2)
     
v = Vector2d(3., -1.)
# The Python interpeter automatically replace abs(v) with Vector2d.__abs__(v)
print(abs(v))
