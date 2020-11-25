# index() is the same as find(), but rise an exception in case of failure
def cut_two_before(input_string, substring):
    """ Cut a string up to two positions before that of the given substring and
    return it """
    pos = input_string.index(substring)
    return input_string[:(pos-1)]

# If the substring exists in the string everything works fine
print(cut_two_before('We all live in a Yellow Submarine', 'Yellow'))
# No silent bug here!
print(cut_two_before('We all live in a Yellow Submarine', 'Red'))
