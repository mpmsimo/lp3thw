"""
ex5.py - More Variables and Printing

Like the title says!

msimo - 2/19/15

Learn Python the hard way!
<learnpythonthehardway.org>

Tested only with Python 3.3.6
"""

string = "string"

print("This is (%s) replacement." % string)
#print("For string replacement, be careful how you (%s) in (%s)." % "pass", "variables")
print("For string replacement, be careful how you (%s) in (%s)." % ("pass", "variables"))
print("This is ({0}) formatting.".format(string))