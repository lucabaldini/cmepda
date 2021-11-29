import math 

class Angle:
    
    # A bunch of useful methods....
    
    @staticmethod
    def rad2deg(rad):
        # The self argument is not passed to a static method
        return rad * 180./math.pi
    
    @staticmethod
    def deg2rad(deg):
        # The self argument is not passed to a static method
        return deg * math.pi / 180.
        
print(Angle.rad2deg(math.pi/2))
print(Angle.deg2rad(45.))
