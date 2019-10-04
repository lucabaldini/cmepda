class Television:
    """ Class describing a televsion.
    """
    def __init__(self, owner):
       """ Class constructor"""
       # Here there is no encapsulation. The attribute can be read and modified
       # freely
       self.owner = owner
       
tv = Television('Batman')
print('This tv belongs to {}'.format(tv.owner)) # Read the attribute
tv.owner = 'Joker' # Change the attribute - this works
print('This tv belongs to {}'.format(tv.owner))
