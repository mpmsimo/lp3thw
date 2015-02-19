"""
ex6.py - More Printing

Modified print statements for Python 3, and commented on how the code works.

msimo - 2/19/15

Learn Python the hard way!
<learnpythonthehardway.org>

Tested only with Python 3.3.6
"""

#Prints the below string
print("Mary had a little lamb.")

#Uses string formatting to replace %s with the string 'snow'.
print("Its fleece was white as %s." % 'snow')

#Prints the below string
print("And everywhere that Mary went.")

#Prints 10 periods '.'
print("." * 10)  # what'd that do?

#Assigns and 'end[x]' variable to a character.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
# I didn't know this before, the comma prints a new line! (same as \n)
# This is to avoid lines larger than 80 characters which is not considered pythonic.
print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)