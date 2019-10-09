class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
   
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector2d(scalar * self.x, scalar * self.y)
        
    def __rmul__(self, scalar):
        # Right multiplication - because a * Vector is different from Vector * a
        return self * scalar # We just call __mul__, no code duplication!
        
    def __str__(self):
        # We keep this to show the results nicely
        return str((self.x, self.y))
     
v, z = Vector2d(3., -1.), Vector2d(-5., 1.)
print(v+z)
print(3 * v)
print(z * 5)
