"""
ex6.py - Strings and Text

Strings&text&
Strings&text&
Strings&text& 
Strings&text&

msimo - 2/19/15

Learn Python the hard way!
<learnpythonthehardway.org>

Tested only with Python 3.3.6
"""

import random

monster_list = ["Target Dummy", "Typhoid Rat", "Orc", "Goblin"]
boolean_list = [True, False]

print("There are {0} types of monsters.\n".format(len(monster_list)))
for monster in monster_list:
	print("{0}".format(monster))
print("\nThose who are green, and those who are not.")
print("I think that is {0}!".format(boolean_list[random.randrange(0,2)]))