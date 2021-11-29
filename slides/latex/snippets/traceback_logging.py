""" Showing the tracebak with logging"""
import logging
logger = logging.Logger('demo')

try:
    with open ('i_do_not_exist.txt') as myfile:
        pass
except FileNotFoundError as e:
    logger.exception(e)
