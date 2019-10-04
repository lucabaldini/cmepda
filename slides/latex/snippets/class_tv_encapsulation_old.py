""" Now we want prevent the owner from being changed using old-style 
encapsulation, with setters and getters"""

class Television:
    """ Class describing a televsion.
    """
    def __init__(self, owner):
       """ Class constructor"""
       self._owner = owner
    
    def get_owner(self):
        """ Old-style getter."""
        return self._owner
        
    def set_owner(self, new_owner):
        """ Old-style setter to control access - in this case preventing the 
        attribute from being changed."""
        print('Nope {}. Do you want to steal my tv?'.format(new_owner))
    
tv = Television('Batman')
# In the following lines we had to change the code!
print('This tv belongs to {}'.format(tv.get_owner()))
tv.set_owner('Joker')
print('This tv belongs to {}'.format(tv.get_owner()))
