import math

class Particle:
    """ Class describing a generic particle.
    """
    def __init__(self, mass, charge=0, name=None, momentum=0.):
        """ Class constructor"""
        self.mass = mass # in MeV
        self.charge = charge # in e
        self.name = name
        self.momentum = momentum # in MeV/c
    
    def energy(self):
        """ Return the energy of the particle in MeV/c^2"""
        return math.sqrt(self.momentum**2. + self.mass**2.)
 
class Electron(Particle):
    """ Class describing an electron. We inherit from Particle
    """
    def __init__(self, momentum=0.):
        """ Derived class constructor. We call the base class constructor"""
        Particle.__init__(self, 0.511, -1., 'e-', momentum)
        
el = Electron(momentum=1.)
print('Energy of {} is {:.4f} MeV/c^2'.format(el.name, el.energy()))
