""" Printing the exception with the 'traceback' module """
import traceback
import os

try:
    with open ('i_do_not_exist.txt') as myfile:
        pass
except FileNotFoundError as e:
    # Log exception to file
    with open ('traceback.log', 'w') as logfile:
        # This will print the full exception
        traceback.print_exception(e.__class__, e, e.__traceback__, file=logfile)
        # Since Python 3.10 this was simplified into:
        # traceback.print_exception(e)
    os.system('cat traceback.log')


