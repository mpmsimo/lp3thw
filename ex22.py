#!/usr/bin/python
"""
ex22.py

Usage: python ex22.py

Author: mpmsimo
Date Created: 8/22/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>
"""
def print_sym(character, description):
    """Puts the symbol within single quotes, and adds a tab after the
character"""
    print("'{0}'\t{1}").format(character, description)

# prints all python symbols that I can think of off the top of my head
print("mathematical operators")
print_sym("+", "Adds a value to another value of the same type")
print_sym("-", "Subtracts a value from another value of the same type")
print_sym("*", "Multiplies a value by an int")
print_sym("/", "Divides a value by an int")
print_sym("%", "Divides a number and returns the remainder")

print("\ncomparison operators")
print_sym("<(=)", "If first value is less than (or equal to) second value")
print_sym(">(=)", "If first value is greater than (or equal to) second value")
print_sym("!=", "If value is not equal")

print("\npython symbols")
print_sym("\\", "Escape character")
print_sym(":", "Indicates the end of a condition")
print_sym("#", "Comments text on line preceding this character")
print_sym("%", "Can be used as a placeholder for a value")
print_sym("-", "Subtracts a value from another value of the same type")

########### Additional Information ###########
"""
"""
