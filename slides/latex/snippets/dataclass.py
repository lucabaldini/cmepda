from dataclasses import dataclass

# Traditional way
class PersonOldStyle:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __repr__(self):
        return f'{self.__class__.__name__}(name=\'{self.name}\', age={self.age}, '\
               f'height={self.height})'
    def __eq__(self, other):
        return (self.name, self.age, self.height) == \
               (other.name, other.age, other.height) 

# With dataclass
@dataclass
class PersonDataclass:
    name : str # Notice the type hint (which is mandatory but not enforced)
    age : int
    height : float

Joe = PersonOldStyle('Joe', 35, 1.84)
print(Joe)
Mary = PersonDataclass('Mary', 28, 1.62)
print(Mary)
