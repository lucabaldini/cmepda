def cut_before(input_string, substring):
    try:
        result = input_string[:(input_string.index(substring))]
        print('This line is not executed if an exception is raised in the try block')
    except ValueError:
        print('This line is executed only if a ValueError is raised in the try block')
    else: # optional!
      print('This line is executed only if no exception is raised in the try block')
      return result
    finally: # optional!
      print('This line is always executed')

cut_before('We all live in a Yellow Submarine', 'Yellow')
cut_before('We all live in a Yellow Submarine', 'Red')
