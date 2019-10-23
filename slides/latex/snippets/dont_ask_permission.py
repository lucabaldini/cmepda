import os

file_path = 'i_do_not_exists.txt'

# Defensive version
if os.path.exists(file_path):
    # What if the file is deleted between these two lines? (by another process)
    # What if the file exists but you don't have permission to open it?
    data_file = open(file_path) 
else:
    # Do something
    print('Oops - file \'{}\' does not exist'.format(file_path))

# Pythonic way - you should prefer this one!
try:
    data_file = open(file_path)
except OSError as e: # Cover more problems than FileNotFoundError
    print('Oops - cannot read the file!\n{}'.format(e))
