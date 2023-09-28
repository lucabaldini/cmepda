
import argparse

from loguru import logger

parser = argparse.ArgumentParser(prog='wordcount',
    description='Count the letter frequency in a text')
parser.add_argument('infile')
parser.add_argument('--plot', action='store_true',
    help='Plot a bar chart of the character frequencies')


def process_file(file_path, plot):
    """Process one file and count the occurrences of each
    charactes.

    Arguments
    ---------
    file_path : str
        Path to the input file.
    """
    logger.info(f'Opening input file {file_path}...')
    with open(file_path) as input_file:
        data = input_file.read()
    logger.info(f'Done, {len(data)} character(s) found.')
    # ... do all the stuff
    if plot:
        logger.info('Plotting stuff...')


if __name__ == '__main__':
    args = parser.parse_args()
    process_file(args.infile, args.plot)
