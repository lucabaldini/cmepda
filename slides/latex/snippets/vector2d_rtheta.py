import math

class Vector2d:
    """ Class representing a Vector2d - storing module and angle."""   
    def __init__(self, module, angle):
        self.module = float(module)
        self.angle = float(angle)
   
    def x(self):
        return self.module * math.cos(self.angle)
       
    def y(self):
        return self.module * math.sin(self.angle)
  
v = Vector2d(3.1622776601683795, -0.3217505543966422)
print(v.module, v.angle)
print(v.x(), v.y())
