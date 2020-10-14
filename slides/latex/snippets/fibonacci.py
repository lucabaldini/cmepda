# Generator function that provides infinte fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# We need to impose a stop condition externally to use it
max_n = 7
fib_numbers = []
for i, fib in enumerate(fibonacci()):
    if i >= max_n:
        break
    else:
        fib_numbers.append(fib)
print(fib_numbers)
      
# Another way to do that  is using 'islice' from itertools
import itertools
# Generator expression
fib_gen = (fib for fib in itertools.islice(fibonacci(), max_n))
print(list(fib_gen))
