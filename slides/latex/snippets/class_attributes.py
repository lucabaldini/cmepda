class Television:
    """ Class describing a televsion.
    """
    NUMBER_OF_CHANNELS = 999 # Class attribute!
    
print(Television.NUMBER_OF_CHANNELS) # We don't need an instance
tv = Television()
print(tv.NUMBER_OF_CHANNELS) # But we can also access it through instances
