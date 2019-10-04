class Animal:
    def sound(self):
        return None

class Dog(Animal):
    def sound(self):
        """ This will shadow the method in the base class"""
        return 'Woof!'
        
class Cat(Animal):
    def sound(self):
        """ This will shadow the method in the base class"""
        return 'Meow!'

class SilentAnimal(Animal):
    pass # I make no sound
     
animals = [Animal(), Cat(), Dog(), SilentAnimal()]
for animal in animals:
    print(animal.sound())
