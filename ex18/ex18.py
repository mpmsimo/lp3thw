"""
ex18.py - Names, Variables, Code, Functions

Usage: python ex18.py

msimo - 2/27/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""
from sys import argv
from os.path import exists

# this one is like your scripts with argv
# Unpacks arg1 and arg2 from the paramater *args.
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {0}, arg2: {1}".format(arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: {0}, arg2: {1}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: {0}").format(arg1)

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

########### Additional Information ###########
"""
"""
