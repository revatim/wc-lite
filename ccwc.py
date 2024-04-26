from os import path
import sys
# sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import argparse
# argparse is a module that makes it easy to write user-friendly command-line interfaces. It is a standard library in Python.
# The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

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


def main(args):
    if args.c:
        process_file(args.c, count_bytes)
    elif args.m:
        process_file(args.m, count_characters)
    elif args.w:
        process_file(args.w, count_words)
    elif args.l:
        process_file(args.l, count_lines)


def process_file(arg, count_func):
    if arg.name != "<stdin>":
        count = count_func(arg.name)
        if (count == None):
            return
        print(f"\t{count} {path.basename(arg.name)}")
    else:
        count = count_func(arg)
        print(f"\t{count}")


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
        stdin_content = sys.stdin.read()
        return len(bytes(stdin_content))
    else:
        return path.getsize(file)


@exception_handler
def count_characters(file):
    # Character is a minimal unit of text. It can be a letter, number, punctuation mark, or a symbol.
    if file is sys.stdin:
        stdin_content = sys.stdin.read().encode("utf-8")
        return len(stdin_content)
    else:
        with open(file, "r") as file_obj:
            content = file_obj.read() # works for UTF-8 / ASCII encoding is that an assumption we should make ?
        return len(content)


@exception_handler
def count_words(file):
    if file is sys.stdin:
        stdin_content = sys.stdin.read().encode("utf-8")
        return len(stdin_content.split())
    else:
        with open(file, "r") as file_obj:
            content = file_obj.read()
        return len(content.split())


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