"""File utilities"""
import os
from glob import glob


def load_files(path, extension='md'):
    """
    A generator that yields contents
    of all files with a certain extension
    in a given folder
    """
    filenames = glob(os.path.join(path, '*.' + extension))

    for filename in filenames:
        with open(filename) as f:
            yield f.read()
