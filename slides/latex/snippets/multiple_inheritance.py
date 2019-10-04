class AudioDevice():
    def play(self, channel):
        print('You are listening to channel n. {}'.format(channel))

class VideoDevice():
    def play(self, channel):
        print('You are looking to channel n. {}'.format(channel))

# Multiple inheritance!
class Television(AudioDevice, VideoDevice):
    def show(self, channel):
        AudioDevice.play(self, channel)
        VideoDevice.play(self, channel)
    
tv = Television()
tv.show(5)
# Is this a good idea?
tv.play(5) # Which one do we get? Why?
# Hint
# print(Television.mro())
