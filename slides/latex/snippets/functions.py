

# Plain
def square(x):
    """Return the square of x.
    """
    return x * x

# Default return value is None
#def 

# More args
#def 

# Default arguments
#def

# Variadic functions
def concatenate(*items):
    """Concatenate the string representations of a series of objects.
    """
    return ''.join(str(item) for item in items)

print(square(2))
print(concatenate())
print(concatenate('U', 2))
print(concatenate('How', ' are', ' you?'))
