import math
from array import array

class Vector:
    """ Classs representing a multidimensional vector"""    
    typecode = 'd'
    
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    def __getitem__(self, index):
        """ That's super easy, as we get to reuse the __getitem__ of array!"""
        return self._components[index]
    
    def __setitem__(self, index, new_value):
        """ Same as __getitem__, we just delegate to the __setitem__ of array"""
        self._components[index] = new_value
    
    def __len__(self):
        """ Did I just write that we like to delegate? """
        return len(self._components)
    
    def __repr__(self):
        components = str(self._components)
        components =  components[components.find('['): -1]
        class_name = type(self).__name__
        return '{}({})'.format(class_name, components)
