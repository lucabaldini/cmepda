class Television:
    """ Class describing a televsion.
    """
    def __init__(self, owner):
       """ Class constructor"""
       self._owner = owner

    def get_owner(self):
        """ Same as the getter"""
        return self._owner

    def set_owner(self, new_owner):
        """ Same as the setter"""
        print(f'Nope {new_owner}. Do you want to steal my tv?')

    # This is where we do the property trick!
    owner = property(fget=get_owner, fset=set_owner)

tv = Television('Batman')
# Notice the difference: this is the same code as before
print(f'This tv belongs to {tv.owner}')
tv.owner = 'Joker' # Change the attribute - this time it does not work
print(f'This tv belongs to {tv.owner}')
