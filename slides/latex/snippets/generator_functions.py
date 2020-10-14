def generator_function_simple():
    print('First call')
    yield 1
    print('Second call')
    yield 2
    print('I am about to rise a StopIteration exception...')

gen = generator_function_simple() # A generator function returns a generator
print(next(gen)) # We stop at the first yield and get the value
print(next(gen)) # Second yield
next(gen) # The third next() will throw StopIteration
