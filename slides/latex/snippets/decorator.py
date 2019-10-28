def print_function_info(func):
    def wrapper(*args, **kwargs):
        print('Calling function \'{}\''.format(func.__name__))
        print('Positional arguments = {}'.format(args))
        print('Keyword arguments = {}'.format(kwargs))
        return func(*args, **kwargs)
    return wrapper

@print_function_info
def some_function(a, b, c=0):
    return a * b + c

# This is equivalent to: some_function = print_function_info(some_function)

print(some_function(1, 2, c=7))
 # Inspecting the function reveals that we are calling the wrapper
print('The name of the function is \'{}\''.format(some_function.__name__))
