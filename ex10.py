"""
ex10.py - What Was That?

Going over the '\'' backslash also known as an escape sequence.
msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

########## ##########
#while True:
print("Printing additional characters and escaping \\")
for i in ["/","-","|","\\","|"]:
    print("%s\r" % i,)