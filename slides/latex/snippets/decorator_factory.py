from functools import wraps

# This is how a generic decorator with arguments looks like

def decorator_factory(*params): # The signature can be anything
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f'Decorator arguments: {params}')
            # some preprocess here
            result = function(*args, **kwargs)
            # some post-process here
            return result
        return wrapper
    return decorator

# usage
@decorator_factory(1, 2, 3)
def f(x):
    return x**2

f(5)
