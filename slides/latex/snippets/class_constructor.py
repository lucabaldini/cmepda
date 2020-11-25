class Television:  
    """ Class describing a televsion.
    """
    def __init__(self, owner):
        """ The special method __init__ is called each time a class istance is
        created.  We can pass arguments to the constructor, just like any 
        function."""
        print('Creating a television instance...')
        self.model = 'Sv32X-553T' # This class attribute is hard-coded
        self.owner = owner # This is set to the value of the argument
    
    def print_info(self): # Let's see
        """ Print the model and owner"""
        message = 'This is television model {}, owned by {}'
        print(message.format(self.model, self.owner))

my_television = Television('Alberto')
my_television.print_info()
batman_television = Television('Batman')
batman_television.print_info()
