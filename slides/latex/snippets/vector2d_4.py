class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector2d(scalar * self.x, scalar * self.y)
        
    def __rmul__(self, scalar):
        return Vector2d(scalar * self.x, scalar * self.y)
        
    def __str__(self):
        return str((self.x, self.y))
     
v = Vector2d(3., -1.)
z = Vector2d(-5., 1.)
print(v+z)
print(3 * v)
print(z * 5)

