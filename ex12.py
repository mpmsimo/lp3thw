"""
ex12.py - Prompting People

Going user input which, differs in Python 3.
raw_input() was changed to input().

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""

# Assigns the age variable age to user input.
age = input("How old are you? ")

# Assigns the height variable age to user input.
height = input("How tall are you? ")

# Assigns the weight variable age to user input.
weight = input("How much do you weigh? ")

# Prints the user input.
print("So, you're {0} old, {1} tall and {2} heavy.".format(age, height, weight))

# In the terminal (Linux - CentOS6.6) type 'pydoc input' to view how the input function works.
# It was suggested to view the open, file, os and sys keywords/libraries with pydoc as well.