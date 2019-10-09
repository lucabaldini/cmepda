import math
from array import array

class Vector:
    """ Classs representing a multidimensional vector"""    
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __iter__(self):
        """ We don't need to code anything... an array is already iterable!"""
        return iter(self._components)
    
v = Vector([5.1, 3.7, -25.])
for component in v:
    print(component)
