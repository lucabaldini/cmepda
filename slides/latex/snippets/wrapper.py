def some_function(a, b):
    print('Executing {} x {}'.format(a, b))
    return a * b
    
def add_n_wrapper(func, n): # We take the wrapped function as argument
    """ This wrapper adds n to the result of the wrapped function"""
    
    def wrapper(*args, **kwargs): 
       """We passs the arguments as *arg, **kwargs, because this is the most
       general form in Python: we can collect any comination of arguments like
       that. Note that we have access to both 'func' and 'n', as they are stored
       in the closure of 'wrapper'"""
       result = func(*args, **kwargs) # Pass the arguments to the wrapped fucntion
       print('Adding {}'.format(n))
       return result + n # Return a modified result in this case
       
    return wrapper # From add_n_wrapper we return the wrapper

function_plus_five = add_n_wrapper(some_function, 5)
print('Result = {}'.format(function_plus_five(2, 3)))
