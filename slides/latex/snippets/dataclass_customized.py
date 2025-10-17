from dataclasses import dataclass
"""
You can control what methods are added to your dataclass through a number of
flags: init, repr, eq, order, unnsafe_hash, frozen...
see https://docs.python.org/3/library/dataclasses.html\#dataclasses.dataclass 
"""
@dataclass(order=True, frozen=True)
class Person:
    name: str
    age: int
    height: float

Joe = Person('Joe', 32, 1.84)
Mary = Person('Mary', 25, 1.62)
print(Joe > Mary)
Joe.age = 33
