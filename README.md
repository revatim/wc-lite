# wc-lite

# CCWC - Custom Count Word Character
This Python script, `ccwc.py`, is a command-line utility that counts the number of bytes/characters/words/lines in a given file. 

## Dependencies
This script requires Python's built-in modules `sys` and `argparse`.

## Use of the Tool

The tool takes a file or a pipe as an input and outputs file measurements according to the chosen option.
The tool tries to follow wc syntax, the usage is as follows:

```python3 main.py ccwc [option] filename```
There are five options supported:

generic: without an option, outputs the number of lines, words and bytes in a file.
-c: outputs the number of bytes in a file.
-l: outputs the number of lines in a file.
-w: outputs the number of words in a file.
-m: outputs the number of chars in a file.
The tool also supports a combination of input, where the ccwc options are as given above, in the form:

```cat filename | python3 main.py ccwc [option]```

### Learning Journey
This script is part of my journey learning programming. I'm working on small projects and challenges to improve my understanding of various programming languages and their standard libraries.

### Contributing
As this is a personal learning project, I'm not currently accepting contributions. However, any feedback or suggestions are welcome!

## Credits

This project is a solution to the [WC-lite challenge](https://codingchallenges.fyi/challenges/challenge-wc) on Coding Challenges. The challenge provided a great opportunity to improve my Python skills and learn more about handling command-line arguments in Python.

### License
This project is licensed under the terms of the MIT license.

