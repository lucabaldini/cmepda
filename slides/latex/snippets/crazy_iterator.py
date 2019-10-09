import random

class CrazyIterator:
    """ Class implementing a crazy iterator"""
    
    def __init__(self, container):
        random.seed(1)
        self._container = container
    
    def __next__(self):
        try:
            # We get one possibility out of len(self._container) to exit
            index = random.randint(0, len(self._container))
            item = self._container[index]
        except IndexError:
            raise StopIteration
        return item
    
    def __iter__(self):
        return self

class CrazyIterable:
    """ Similar to a simple iterable, but with a twist... """
    
    def __init__(self, *elements):
        self._elements = list(elements)
    
    def __iter__(self):
        return CrazyIterator(self._elements)
