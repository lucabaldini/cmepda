# index() is the same as find(), but rise an exception in case of failure
def cut_before(input_string, substring):
    """ Cut a string from the beginning up to the position before that of
    the given substring, then return it """
    pos = input_string.index(substring)
    return input_string[:(pos)]

# If the substring exists in the string everything works fine
print(cut_before('We all live in a Yellow Submarine', 'Yellow'))
# No silent bug here!
print(cut_before('We all live in a Yellow Submarine', 'Red'))
