Module: basic Python
Assignment #2 (Set 30, 2021)

--- Goal
Write a program to explore the properties of a few elementary Particles.
The program must contain a Base class Particle and two Child classes, Proton and Alpha, that inherit from it.

--- Specifications
- instances of the class Particle must be initialized with their mass, charge, and name
- the class constructor must also accept (optionally) and store one and only one of the following quantities: energy, momentum, beta or gamma
- whatever the choice, the user should be able to read and set any of the
  above mentioned quantities using just the '.' (dot) operator e.g.
  print(my_particle.energy), my_particle.beta = 0.5
- attempts to set non physical values should be rejected
- the Particle class must have a method to print the Particle information in
  a formatted way
- the child classes Alpha and Protons must use class attributes to store their mass, charge and name
