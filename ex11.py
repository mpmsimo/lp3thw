"""
ex11.py - Asking Questions

Going user input which, differs in Python 3.
raw_input() was changed to input().

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""

# This will ask the user their age.
print("How old are you?",)
age = input()

# This will ask the user how tall they are.
print("How tall are you?",)
height = input()

# This will ask the user how much they weigh.
print("How much do you weigh?",)
weight = input()

# This will print the user input captured earlier in the program.
print("So, you're {0} old, {1} tall and {2} heavy.".format(age, height, weight))