# Here we create a lambda function and assign a name to it (ironically)
multiply = lambda x, y: x * y
# Use it
print(multiply(5, -1))

# Typical use is inside generator functions
numbers = range(10)
squares = list(map(lambda n: n**2, numbers))
print(squares)

# However, remeber that you can do the same with list comprehension
squares = [n**2 for n in numbers]
print(squares)
