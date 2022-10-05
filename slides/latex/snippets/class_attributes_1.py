class Television:
    """ Class describing a televsion.
    """
    pass

tv = Television()
# Add an attribute manually, with a simple assignment
# Attributes are accessed through the '.' (dot) operator
tv.channel = 1
print (tv.channel)
# This attribute is not shared with other instances of the class
another_tv = Television()
print(another_tv.channel)
