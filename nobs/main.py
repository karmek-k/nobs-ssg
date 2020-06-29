"""This module contains the main function"""
import argparse

from colorama import init as colorama_init, Fore, Back, Style
from pyfiglet import Figlet


def get_args():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    return args


def main():
    """This function is executed when the CLI is started"""
    # Initialize colorama
    colorama_init()

    # Print some fancy text
    ascii_art = Figlet(font='slant').renderText('nobs').rstrip()
    print(Fore.CYAN, ascii_art, Style.RESET_ALL)

    # Display version
    try:
        version = __version__
    except NameError:
        version = 'UNDEFINED'
    print(f'{Fore.GREEN}{Style.BRIGHT}Nobs-SSG - version {version}{Style.RESET_ALL}')

    # Parse command-line arguments
    print()
    args = get_args()


# later main() will be executed by a separate script
if __name__ == '__main__':
    main()