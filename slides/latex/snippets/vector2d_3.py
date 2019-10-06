import math

class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
    def __repr__(self):
        # We don't want to hard-code the class name, so we dynamically get it
        class_name = type(self).__name__
        return ('{}({}, {})'.format(class_name, self.x, self.y))
        
    def __str__(self):
        # We convert the coordinates to a tuple (notice the 2 parenthesis) 
        # and use the __str__ method of tuples, which already provides a nice
        # formatting
        return str((self.x, self.y))
     
v = Vector2d(3., -1.)
print(v) # Is the same as print(str(v))
print(repr(v))
print('I got {} with __str__() and {!r} with __repr__'.format(v, v))
