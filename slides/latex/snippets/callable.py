class CallCounter:
  
    """Wrap a generic function and count the number of times it is called"""
    
    def __init__(self, func):
        # We accept as input a function and store it (privately)
        self._func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        """ This is the method doing the trick. We use *args and **kwargs to
        pass all possible arguments to the function that we are wrapping"""
        # We increment the counter
        self.num_calls += 1
        # And here we just return whatever the wrapped function returns
        return self._func(*args, **kwargs)
    
    def reset(self):
        self.num_calls = 0
