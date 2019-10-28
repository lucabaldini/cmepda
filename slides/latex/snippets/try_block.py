try:
    with open ('i_do_not_exist.txt') as lab_data_file:
        """ Do some process here...
        ...
        ...
        """
except FileNotFoundError as e: # we assign a name to the the exception 
    print(e)


# We can be less specific by catching a parent exception
try:
    with open ('i_do_not_exist.txt') as lab_data_file:
        """ Do some process here...
        ...
        ...
        """
except OSError as e: # OSError is a parent class of FileNotFoundError
    print(e)

# catching Exception will catch almost everything!
