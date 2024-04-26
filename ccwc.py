from os import path
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
        if args.c.name != "<stdin>":
            count = count_bytes(args.c.name)
            if (count == None):
                return
            print(f"\t{count} {path.basename(args.c.name)}")
        else:
            count = count_bytes(args.c)
            print(f"\t{count}")
    elif (args.m):
        if args.m.name != "<stdin>":
            count = count_characters(args.m.name)
            print(f"\t{count} {path.basename(args.m.name)}")
        else:
            count = count_characters(args.m)
            print(f"\t{count}")
    elif (args.w):
        if args.w.name != "<stdin>":
            count = count_words(args.w.name)
            print(f"\t{count} {path.basename(args.w.name)}")
        else:
            count = count_words(args.w)
            print(f"\t{count}")
    elif (args.l):
        if args.l.name != "<stdin>":
            count = count_lines(args.l.name)
            if (count == None):
                return
            print(f"\t{count} {path.basename(args.l.name)}")
        else:
            count = count_lines(args.l)
            print(f"\t{count}")
    return None

def exception_handler(func):
    def wrapper(*args, **kwargs):
        file = kwargs.get('file', args[0] if args else None)
        try:
            return func(*args, **kwargs)
        # The argparse module in Python tries to open the file when it parses the command-line arguments when the file doesn't exist or cannot be opened for some other reason, it raises an error.
        # FileNotFound, IsADirectory, IOError, PermissionError
        except UnicodeDecodeError:
            print(f"File: {path.basename(file)} contains invalid encoding.")
        except MemoryError:
            print(f"File: {path.basename(file)} is too large to be processed.")
        except OSError:
            print(f"File: {path.basename(file)} cannot be opened. An error occurred: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper


@exception_handler
def count_bytes(file):
    """
    This function counts the number of bytes in a file
    Args:
        file: File object
    
    Returns:
        int: Number of bytes in the file
    
    Raises: 
        UnicodeDecodeError: If the file contains invalid encoding
        MemoryError: If the file is too large to be processed
        OSError: If the file cannot be opened
    """
    if file is sys.stdin:
        stdin_content = sys.stdin.read().encode("utf-8")
        return len(bytes(stdin_content))
    else:
        return path.getsize(file)


@exception_handler
def count_characters(string):
    raise NotImplementedError("Function not implemented")


@exception_handler
def count_words(string):
    raise NotImplementedError("Function not implemented")


@exception_handler
def count_lines(file):
    if file is sys.stdin:
        stdin_content = sys.stdin.read().encode("utf-8")
        lines = stdin_content.splitlines()
        return len(lines)
    else:
        with open(file, "r") as file_obj:
            total_lines = sum(1 for _ in file_obj)
        return total_lines

   
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