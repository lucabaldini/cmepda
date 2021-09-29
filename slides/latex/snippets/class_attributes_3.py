class Television:
    """ Class describing a televsion.
    """
    NUMBER_OF_CHANNELS = 999 # This is a class attribute   
    
# We don't need an instance to access class attributes
print(Television.NUMBER_OF_CHANNELS)
# But we can also access it through instances
tv = Television()
print(tv.NUMBER_OF_CHANNELS)

# Changing the attribute in the class namespace will change it for every instance
another_tv = Television()
Television.NUMBER_OF_CHANNELS = 998
print(another_tv.NUMBER_OF_CHANNELS)
# But assigning to that attribute in an instance namespace will create a copy!
# Result: the other instances won't be affected!
tv.NUMBER_OF_CHANNELS = 997
print(another_tv.NUMBER_OF_CHANNELS)
