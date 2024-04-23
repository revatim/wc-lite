import sys
# sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import argparse
# argparse is a module that makes it easy to write user-friendly command-line interfaces. It is a standard library in Python.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

def main(args):
    """_summary_

    Args:
        args (_type_): _description_

    Returns:
        _type_: _description_
      
    Raises:
        _type_: _description_
    """
    if (args.c):
        # todo: identify 
        print("Count Characters")
    return None

def count_bytes(file):
    """
    This function counts the number of bytes in a file
    Args:
        file: File object
    
    Returns:
        int: Number of bytes in the file
    
    Raises: 
        FileNotFoundError: If the file is not found
        IsADirectoryError: If the file is a directory
        IOError: If there is an error reading the file (e.g., due to corruption)
        UnicodeDecodeError: If the file contains invalid encoding
        OSError: If the file is not accessible
    """
    
    return None

def count_characters(string):
    raise NotImplementedError("Function not implemented")

def count_words(string):
    raise NotImplementedError("Function not implemented")
  
def count_lines(string):
    raise NotImplementedError("Function not implemented")
    
def arguments_setup():
    """
    This function sets up the arguments for the script, and provides help for user to understand the arguments
    Flags Available: 
    """
    parser = argparse.ArgumentParser(description="Count the number of characters/words/lines in a file")
    
        # -c: Flag Argument Counts the number of bytes in each input file
        # Optional Argument are prefixed with - or -- and can be used in any order
    parser.add_argument(
        "-c",
        nargs="?", # The number of command-line arguments that should be consumed in this case 0 or 1.
        type=argparse.FileType("r"), # Opens file with read permissions
        const=sys.stdin,
        help="Count the number of bytes in each input file. If no file is provided, read from standard input.",
    )
    
    # -m: Flag Argument Counts the number of characters in each input file
    parser.add_argument(
        "-m",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="Count the number of characters in each input file. If no file is provided, read from standard input.",
    )
    
     # -w: Flag Argument Counts the number of words in each input file
    parser.add_argument(
        "-w",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="Count the number of words in each input file. If no file is provided, read from standard input.",
    )
    
    # -l: Flag Argument Counts the number of lines in each input file
    parser.add_argument(
        "-l",
        nargs="?",
        type=argparse.FileType("r"),
        const=sys.stdin,
        help="Count the number of lines in each input file. If no file is provided, read from standard input.",
    )
    
    # -t: Flag Argument to specify the type of input: file or string
    parser.add_argument(
        '-t', 
        '--type', 
        choices=['file', 'string'], 
        default='file', 
        help='Type of input: "file" or "string"'
    )

    # Positional Argument to take the input file name
    # Positional Arguments are mandatory and their order matters
    parser.add_argument(
        "input_file",
        nargs="?",
        help="A positional argument which can take a file name or string as input. If no input is provided, read from standard input.",
    )

	# Converts command-line arguments into an object with attributes
    return parser.parse_args()

if __name__ == "__main__":
    args = arguments_setup()
    main(args)