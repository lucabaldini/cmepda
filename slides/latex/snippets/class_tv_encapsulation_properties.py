""" This time with the special @ syntax, which is much more concise and elegant. """

class Television:
    """ Class describing a televsion.
    """
    def __init__(self, owner):
       """ Class constructor"""
       # Old-style encapsulation, using setters and getters. Never do that.
       self._owner = owner
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
       """ This function must be called 'owner'"""
       print('Nope {}. Do you want to steal my tv?'.format(new_owner))
 
tv = Television('Batman')
# Again: this is the same code as before
print('This tv belongs to {}'.format(tv.owner)) 
tv.owner = 'Joker'
print('This tv belongs to {}'.format(tv.owner))
