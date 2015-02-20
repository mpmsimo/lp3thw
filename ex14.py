"""
ex14.py - Prompting and Passing

Learning how to use command line arguments with sys.argv.
Usage: python ex14.py msimo

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""
# Importing argv from the Python sys module
from sys import argv

# Requires user_name as a command line argument.
script, user_name = argv

# I personally like the 'append' style of prompt.
prompt = '>> '

# Says hello to the user (sys.argv[1]), and identifies the script (sys.argv[0]) that is running.
print("Hi {0}, I'm the {1} script.".format(user_name, script))

print("I'd like to ask you a few questions.")

# Script asks the user if it's likable.
print("Do you like me {0}?".format(user_name))
likes = input(prompt)

# Asks the user where they live.
print("Where do you live {0}?".format(user_name))
lives = input(prompt)

# Ask the user about their computer.
print("What kind of computer do you have?")
computer = input(prompt)

# Recaps information provided by the user.
print("""
Alright, so you said {0} about liking me.
You live in {1}.  Not sure where that is.
And you have a {2} computer.  Nice.
""".format(likes, lives, computer))

########## Additional Code ##########
# Although, I have not played Zork personally. I am familar with the game as it was mentioned by Chris Hardwick to Bill Gates on Nerdist Podcast 627.
