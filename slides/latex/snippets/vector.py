import math
from array import array

class Vector:
    """ Classs representing a multidimensional vector"""
    TYPE_CODE = 'd' #We use a class attribute to save the code required for array

    def __init__(self, components):
        self._components = array(self.TYPE_CODE, components)

    def __repr__(self):
        """ Calling str() of an array produces a string like
        array('d', [1., 2., 3., ...]). We remove everything outside the
        square parenthesis and add our class name at the beginning."""
        components = str(self._components)
        components =  components[components.find('['): -1]
        return f'{self.__class__.__name__}({components})'

    def __str__(self):
         return str(tuple(self._components)) # Using str() of tuples as before

v = Vector([5., 3., -1, 8.])
print(v)
print(repr(v))
