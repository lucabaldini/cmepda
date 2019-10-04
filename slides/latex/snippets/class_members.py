class Television:
    """ Class describing a televsion.
    """
    model = "Sv32X-553T" # This is a class variable

print(Television.model) # We don't need an instance to access it
tv = Television()
print(tv.model) # We can access it also through instances
