class Television:
    """ Class describing a televsion.
    """
    def add_an_attribute(self):
        """ Add a class attribute (remember the meaning of 'self') """
        self.current_channel = 1

tv = Television()
# Add an attribute from inside a class method
tv.add_an_attribute()
print (tv.current_channel)

# Again, attributes are not shared
another_tv = Television()
another_tv.add_an_attribute()
# Changing the attribute for one will not affect other instances of the class
tv.current_channel = 5
# The following line will print 1, not 5
print(another_tv.current_channel)
