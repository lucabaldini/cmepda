class Television:
    """ Class describing a televsion.
    """
    def __init__(self, owner):
       """ Class constructor"""
        # Single underscore - tells the user he shouldn't access the variable
        # directly outside the class
       self._model = 'Sv32X-553T'
        # Double underscore - python will prepend _Television to the name
       self.__owner = owner
    

tv = Television('Alberto')
 # The following line is bad practice, but it's technically possible
print(tv._model)
 # Even with two underscores I can still access it if I know the "trick"
print(tv._Television__owner)
