import time 
from functools import wraps

def clocked(func):
    """ We use functools.wraps to keep the original function name and docstring"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        tstart = time.clock()
        result = func(*args, **kwargs)
        exec_time = time.clock() - tstart
        print('Function {} executed in {} s'.format(func.__name__, exec_time))
        return result
    return wrapper

@clocked
def square_list(input_list):
    """ Return the square of a list"""
    return [item**2 for item in input_list]

# Make sure the function name and docstring look the same
print('\'{}\': {}'.format(square_list.__name__, square_list.__doc__))
square_list(range(2000000))
