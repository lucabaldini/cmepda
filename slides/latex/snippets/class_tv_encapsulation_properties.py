class Television:
    """ Class describing a televsion.
    """
    def __init__(self, owner):
       """ Class constructor"""
       self._owner = owner # owner is private
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner):
       """ Make the attribute read-only by acting on the setter"""
       print('Nope {}. Do you want to steal my tv?'.format(new_owner))
 
tv = Television('Batman')
print('This tv belongs to {}'.format(tv.owner)) 
tv.owner = 'Joker'
print('This tv belongs to {}'.format(tv.owner))
