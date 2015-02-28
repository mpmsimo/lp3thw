"""
ex21.py - Functions Can Return Something

Usage: python ex21.py

msimo - 2/27/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""

# Simple addtion function that adds paramaters a and b together, returns the sum of a and b.
def add(a, b):
    print("ADDING {0} + {1}".format(a, b))
    return a + b

# Subtracts a from b and returns the difference.
def subtract(a, b):
    print("SUBTRACTING {0} - {1}".format(a, b))
    return a - b

# Multiplies a and b, returns the product.
def multiply(a, b):
    print("MULTIPLYING {0} * {1}".format(a, b))
    return a * b

# Divides a and b, returns the quotient.
def divide(a, b):
    print("DIVIDING {0} / {1}".format(a, b))
    return a / b

print("Let's do some math with just functions!")

# 30+5 = 35
age = add(30, 5)

# 78-4 = 74
height = subtract(78, 4)

# 90*2 = 180
weight = multiply(90, 2)

# 100/2 = 50 (That's a low IQ, what are you trying to say!?)
iq = divide(100, 2)

# Prints string with the values recorded above.
print("Age: {0}, Height: {1}, Weight: {2}, IQ: {3}".format(age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

########### Additional Information ###########
"""
"""
