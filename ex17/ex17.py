"""
ex17.py - More Files

Usage: python ex17.py

msimo - 2/20/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

OS: CentOS 6.6
Tested with Python 3.3.6
"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line, how?
indata = open(from_file).read()

print("The input file is {0} bytes long".format(len(indata)))

print("Does the output file exist? {0}".format((to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
########### Additional Information ###########
"""
"""