class Television:
    """ Class describing a televsion.
    """
    def __init__(self):
       """ Class constructor"""
       self.is_on = False
       self.current_channel = 1       
    
    def turn_on(self):
        """ Turn on the tv (I omit the turn_off() method for brevity)"""
        print('Turning on!')
        self.is_on = True

    def next_channel(self):
        """ Go to next channel. Works only if the tv is on! """
        if (self.is_on):
            self.current_channel += 1

tv = Television()
tv.next_channel() # This will do nothing
print(tv.current_channel)
tv.turn_on()
tv.next_channel() # This will work
print(tv.current_channel)
