"""
ex15.py - Reading Files

Learning how to read from a file.
Usage: python ex15.py ex14.py

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""
# Importing argv from the Python sys module.
from sys import argv

# Asks for a filename in sys.argv[1].
script, filename = argv

# Opens the file 'filename' as txt.
txt = open(filename)

# Prints the filename, followed by the contents of the file.
print("Here's your file {0}:".format(filename))
print(txt.read())

# Prompts the users for another filename.
print("Type the filename again:")
file_again = input(">> ")

# Opens then prints the file contents.
txt_again = open(file_again)
print(txt_again.read())

""" Additional Information """
'''
6. Using IDLE we can open a file 
>>> f = open("ex14.py")
>>> print(f.read())

7. Closing a file.
>>> f.close()

After the file is closed try printing the contents of the file in IDLE? What happens?
'''