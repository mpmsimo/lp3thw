"""
ex20.py - Functions and Files

Usage: python ex20.py file1.txt

msimo - 2/27/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""
from sys import argv

# Unpacks the script and input file as the first two sys arguments.
script, input_file = argv

# Function that takes in a filename, and reads the content of the file.
def print_all(f):
    print(f.read())

# Seeks a new position within the file, 0 refers to the beginning of the file.
def rewind(f):
    f.seek(0)

# Prints the linecount value, as well as the contents of file 'f'.
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

########### Additional Information ###########
"""
"""
