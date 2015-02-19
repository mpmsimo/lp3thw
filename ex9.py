"""
ex9.py - More Printing

Modified ex9 for Python 3, and commented on how the code works.

msimo - 2/19/15

Learn Python the hard way!
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""

# Creates string days with the below string.
days = "Mon Tue Wed Thu Fri Sat Sun"

# Creates string months, where each month is seperated by an newline character.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints value of days, expected result should be a string on one line.
print("Here are the days: ", days)
# Prints value of months, expected result should be one string across seven lines.
print("Here are the months: ", months)

#Prints a multi-line comment, expected result should be four strings across four lines.
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")