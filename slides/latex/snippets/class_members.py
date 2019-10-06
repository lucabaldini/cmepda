class Television:
    """ Class describing a televsion.
    """
    def add_a_class_member(self):
        """ Add a class member (remember the meaning of 'self') """
        self.current_channel = 1

tv = Television()
tv.add_a_class_member()

# Class members are accessed through the '.' (dot) operator
print (tv.current_channel)

# Each instance gets its own copy of the members
another_tv = Television()
another_tv.add_a_class_member()
# Changing the member for one will not affect other instances of the class
tv.current_channel = 5
# The following line will print 1, not 5
print(another_tv.current_channel)
