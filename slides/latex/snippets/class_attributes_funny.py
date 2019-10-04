class Television:
    """ Class describing a televsion.
    """
    NUMBER_OF_CHANNELS = 999 # Class attribute!
    
tv = Television()
another_tv = Television()
# Changing the attribute in the class namespace will change it for every instance
Television.NUMBER_OF_CHANNELS = 998
print(another_tv.NUMBER_OF_CHANNELS)
# But assigning to that attribute in an instance namespace will create a copy!
# Result: the other instances won't be affected!
tv.NUMBER_OF_CHANNELS = 997
print(another_tv.NUMBER_OF_CHANNELS)
