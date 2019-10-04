class Engine:
    """ Class describing a fuel engine
    """
    def start(self):
        """ Start the engine """
        print('Broom broom!')

class Car:
    """Class describing a car.
    """
    def __init__(self):
        self.engine = Engine()
      
    def drive(self):
        """ Start the car """
        self.engine.start()
    

ferrari = Car()
ferrari.drive()
