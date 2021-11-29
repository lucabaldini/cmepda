from functools import wraps

def repeat(num_times):
    """ Repeat a function call a given number of times"""
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                function(*args, **kwargs)
        return wrapper
    return decorator

# usage
@repeat(num_times=4)
def greet():
    print('Hello!')

greet()
