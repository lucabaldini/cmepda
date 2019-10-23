""" range() is a function that returns a generator in Python 3. The list of 
numbers never exists entirely, they are created ine at a time.
Note: In Python 2 range() does create the full list at the beginning. 
There used to be a xrange() function for lazy generation, which is now 
deprecated in Python 3. """
for i in range(4):  # generators act like iterators in for loop
    print(i)

data = [12, -1, 5]
square_data_generator = (x**2 for x in data) # generator expression!
for square_datum in square_data_generator: # again, 
    print(square_datum)
