"""
ex13.py - Parameters, Unpacking, Variables

Learning how to use command line arguments with sys.argv.
Usage: python ex13.py 1 3.3.6 "hello world"

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""
# Importing libraries should be done in three steps
# Importing Python libraries
from sys import argv

# Importing third party libraries, for example:
# import json, paramiko, MySQLdb, requests

# Importing custom written modules, for example:
# import ex12, ex3

# Don't forget that we start at 0 as the first item in a list and count upwards from there.

# Unpacks the following variables 
# script = sys.argv[0], first = sys.argv[1], second = sys.argv[1], third = sys.argv[2]
script, first, second, third = argv

# Prints sys.argv[0] which is the name of the file currently running.
print("The script is called:", script)

# Prints sys.argv[1]
print("Your first variable is:", first)

# Prints sys.argv[2]
print("Your second variable is:", second)

# Prints sys.argv[3]
print("Your third variable is:", third)

########## Additional code ##########
print("\nWhat would you like for the fourth variable to be?",)
fourth = input()
print("Your fourth variable is:", fourth)