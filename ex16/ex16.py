"""
ex16.py - Reading and Writing Files

Learning how read a file and then write to a file.

Change directory to the ex16 folder.
cd ex16

Usage: python ex16.py ex16.txt

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

OS: CentOS 6.6
Tested with Python 3.3.6
"""
from sys import argv

script, filename = argv

print("We're going to erase {0}.".format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

# Calling w already truncates the file so calling target.truncate() is not needed.
# If we used w+, this would would need to call the truncate() function, unless the file did not exist.
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write((line1 + "\n" + line2 + "\n" + line3 + "\n"))

print("And finally, we close it.")
target.close()

########### Additional Information ###########
"""
First we need to create a new directory for the exercise.
mkdir ex16

Let's move the script to the newly created directory.
mv ex16.py ex16

Afterwards we can create a new file. (This step is optional as w and w+ create the file if it doesn't exist.)
touch ex16/ex16.txt

Let's add some text, and then append another line.
echo "Hello world" > ex16/ex16.txt && echo "This is another line" >> ex16/ex16.txt

Just to be sure, let's check to see if the text was actually written to file.
cat ex16/ex16.txt

Looks good! Now let's run the script against the newly created file.
"""