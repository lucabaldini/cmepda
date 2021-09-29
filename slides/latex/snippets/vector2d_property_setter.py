import math

class Vector2d:
    """ Class representing a Vector2d - storing module and angle."""   
    def __init__(self, module, angle):
        self.module = float(module)
        self.angle = float(angle)
   
    @property
    def x(self):
        return self.module * math.cos(self.angle)
        
    @property
    def y(self):
        return self.module * math.sin(self.angle)
    
    @x.setter
    def x(self, x): # this function must be called as the property
        """ Here we actually need to update module and angle"""
        self.module, self.angle = math.sqrt(x**2 + self.y**2),\
                                  math.atan2(self.y, x)
        
v = Vector2d(3.1622776601683795, -0.3217505543966422)
print(v.x)
v.x = 1.
print(v.x)
