import math

class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        return ((self.x, self.y) == (other.x, other.y)) 
        
    def __ge__(self, other):
        return abs(self) >= abs(other)
        
    def __lt__(self, other):
        return abs(self) < abs(other)

v = Vector2d(3., -1.)
z = Vector2d(-5., 1.)
print(v >= z, v == z, v < z)
