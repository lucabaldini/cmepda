""" Printing the traceback with the 'traceback' module """
import traceback
import sys

try:
    with open ('i_do_not_exist.txt') as myfile:
        pass
except FileNotFoundError as e:
    # The tracebak is stored as an attribute of the exception
    # By default print_tb() output is redirected to the stderr, but you can 
    # change that by setting the 'file' argument
    traceback.print_tb(e.__traceback__, file=sys.stdout)
