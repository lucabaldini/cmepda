from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Person:
    name: str
    age: int
    height: float

Joe = Person('Joe', 32, 1.84)
Mary = Person('Mary', 25, 1.62)
print(Joe > Mary)
Joe.age = 33
