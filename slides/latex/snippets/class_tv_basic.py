# Here we define the class
class Television:
    """ Television class. I will follow the convention of starting class names
    with an uppercase. """
    pass # oops we have no code yet!

"""To create instances of a class in python we use the parenthesis operator '()'.
The syntax is similar to calling a function -- which is actually what is 
happening behind the scenes, as we will see later"""
my_television = Television() # my_television is an instance of the class Television

print(type(my_television)) # Check its type

your_television = Television() # And this is another instance

# Let's check that they are really two different objects
print(my_television is not your_television)
