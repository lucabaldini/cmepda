class Television:
    """ Class describing a televsion.
    """
    def turn_on(self): # Class method
        """All the class methods get the object istance as their first argument.
        It is customary to call this argument 'self', though is not required
        by the language rules (you can call it 'pippo' and it will work 
        just as well)
        """
        print('Turning on!')

tv = Television()
# Class methods and members are accessed through the '.' (dot) operator
tv.turn_on()

