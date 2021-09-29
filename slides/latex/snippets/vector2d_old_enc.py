import math

class Vector2d:
    """ Class representing a Vector2d. Old-style encapsulation."""   
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
   
    def x(self):
        return self._x
       
    def y(self):
        return self._y
   
    def module(self):
        return math.sqrt(self._x**2 + self._y**2)
       
    def angle(self):
        return math.atan2(self._y, self._x)
  
v = Vector2d(3., -1.)
print(v.x(), v.y())
print(v.module(), v.angle())
