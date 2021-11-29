def cut_before(input_string, substring):
    try:
        result = input_string[:(input_string.index(substring))]
        print('This line is not executed if an exception is raised in the try block')
        return result
    # Catch the correct exception type with 'except'
    except ValueError:
        print('This line is executed only if a ValueError is raised in the try block')

cut_before('We all live in a Yellow Submarine', 'Yellow')
cut_before('We all live in a Yellow Submarine', 'Red')
