class Television:
    """ Class describing a televsion.
    """
    def turn_on(self, channel=1): # Class method
        """All the class methods get the object instance as their first argument.
        It is customary to call this argument 'self', though is not required
        by the language rules (you can call it 'pippo' and it will work
        just as well)
        """
        print(f'Turning on {self}')
        print(f'Showing channel {channel}')

tv = Television()
# Class methods and members are accessed through the '.' (dot) operator
# You must not pass the 'self' argument, it is added automatically!
tv.turn_on(channel=3)
