class Vector2d:
    """ Class representing a Vector2d """   
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
   
    def __repr__(self):
        # We don't want to hard-code the class name, so we dynamically get it
        class_name = type(self).__name__
        return ('{}({}, {})'.format(class_name, self.x, self.y))
        
    def __str__(self):
        """ We convert the coordinates to a tuple so that we can reuse the
        __str__ method of tuples, which already provides a nice formatting.
        Notice the two parenthesis: this line is equivalent to:
        temp_tuple = (self.x, self.y)
        return str(temp_tuple)
        """
        return str((self.x, self.y))
     
v = Vector2d(3., -1.)
print(v) # Is the same as print(str(v))
print(repr(v))
print('I got {} with __str__ and {!r} with __repr__'.format(v, v))
