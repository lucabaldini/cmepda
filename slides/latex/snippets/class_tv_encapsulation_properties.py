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
       print(f'Nope {new_owner}. Do you want to steal my tv?')

tv = Television('Batman')
print(f'This tv belongs to {tv.owner}')
tv.owner = 'Joker'
print(f'This tv belongs to {tv.owner}')
