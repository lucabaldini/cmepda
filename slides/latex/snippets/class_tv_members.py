class Television:
    """ Class describing a televsion.
    """
    def add_a_class_member(self):
        """ Add a class member """
        self.current_channel = 1

tv = Television()
tv.add_a_class_member()

# Class members are accessed through the '.' (dot) operator
print (tv.current_channel)

# You can manipulate the value of class members as usual
tv.current_channel = 5
print(tv.current_channel)

# The change will not affect other instances of the class
another_tv = Television()
another_tv.add_a_class_member()
# The following line will print 1, not 5
print(another_tv.current_channel)
