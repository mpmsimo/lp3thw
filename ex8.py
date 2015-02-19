"""
ex8.py - More Printing

Modified ex8 for Python 3, and commented on how the code works.

msimo - 2/19/15

Learn Python the hard way!
<learnpythonthehardway.org>

Tested only with Python 3.3.6
"""

# %r prints raw data which I agree is great for debugging.
formatter = "%r %r %r %r"

# Prints integers 1, 2, 3, and 4.
print(formatter % (1, 2, 3, 4))

# Prints strings "one", "two", "three" and "four".
print(formatter % ("one", "two", "three", "four"))

# Prints boolean keywords
print(formatter % (True, False, False, True))

# Prints each value of formatter (%r), with an instance of formatter - Expects 16 %r's.
# each %r in the initial formatter expression, will be replaced with four %r's as defined in formatter.
print(formatter % (formatter, formatter, formatter, formatter))

# Prints raw data for four strings.
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))