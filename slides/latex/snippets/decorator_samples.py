from functools import wraps
import time

def print_function_info(func):
    """ Print function arguments"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling function \'{}\''.format(func.__name__))
        print('Positional arguments = {}'.format(args))
        print('Keyword arguments = {}'.format(kwargs))
        return func(*args, **kwargs)
    return wrapper

def clocked(func):
    """ Measure execution time"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        tstart = time.clock()
        result = func(*args, **kwargs)
        exec_time = time.clock() - tstart
        print('Function {} executed in {} s'.format(func.__name__, exec_time))
        return result
    return wrapper

def repeat(num_times):
    """ Repeat a function call a given number of times"""
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                function(*args, **kwargs)
        return wrapper
    return decorator
