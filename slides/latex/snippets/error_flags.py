# The 'find()' method for strings in python uses an error flag
text = 'elephant'
print(text.find('p')) # upon success returns the position of the substring
print(text.find('d')) # returns -1 if the substring is not found

# Why is this dangerous?
def cut_before(input_string, substring):
    """ Cut a string from the beginning up to the position before that of
    the given substring, then return it """
    pos = input_string.find(substring)
    return input_string[:(pos)]

# If the substring exists in the string everything works fine
print(cut_before('We all live in a Yellow Submarine', 'Yellow'))
# What will be the output here?
print(cut_before('We all live in a Yellow Submarine', 'Red'))
