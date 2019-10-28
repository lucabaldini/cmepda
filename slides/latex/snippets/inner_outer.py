def outer():   
    def inner(): # Defining the inner function inside the outer function
        print('Inner function')
        return # End of the inner function
    return inner # Inner is the output of outer
    
my_func = outer() # my_func is now referncing 'inner'
print(my_func.__name__)
my_func() # Calling my_func is equal to calling 'inner'

def outer2():
    some_string = 'Hello!'
    def inner():
        # We have access to the variables in the outer function!
        print(some_string)
    return inner
    
my_other_func = outer2()
my_other_func()
