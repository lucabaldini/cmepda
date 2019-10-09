class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
        
    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self
        
    def __str__(self):
        return str((self.x, self.y))
     
v = Vector2d(3., -1.)
z = Vector2d(-5., 1.)
v += z
print(v)
v *= z
print(v)
