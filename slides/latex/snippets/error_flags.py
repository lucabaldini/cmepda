# The 'find()' method for strings in python uses an error flag
text = 'elephant'
print(text.find('p')) # upon success returns the position of the substring
print(text.find('d')) # returns -1 if the substring is not found

# Why is this dangerous?
def cut_two_before(input_string, substring):
    """ Cut a string up to two positions before that of the given substring and
    return it """
    pos = input_string.find(substring)
    return input_string[:(pos-1)]

# If the substring exists in the string everything works fine
print(cut_two_before('We all live in a Yellow Submarine', 'Yellow'))
# What will be the output here?
print(cut_two_before('We all live in a Yellow Submarine', 'Red'))
