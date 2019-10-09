class SimpleIterator:
    """ Class implementing a super naive iterator"""
    
    def __init__(self, container):
        self._container = container
        self.index = 0
    
    def __next__(self):
        try:
            # Note: here we are calling the __getitem__ method of self._container
            item = self._container[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return item
    
    def __iter__(self):
        return self
        
class SimpleIterable:
    """ A very basic iterable """
    
    def __init__(self, *elements):
        # We use a list to store elements internally.
        # This provide us with the __getitem__ function
        self._elements = list(elements)
    
    def __iter__(self):
        return SimpleIterator(self._elements)
