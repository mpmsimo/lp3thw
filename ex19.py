"""
ex19.py - Functions and Variables

Usage: python ex19.py

msimo - 2/27/15

Learn Python the hard way by Zed A. Shaw
<learnpythonthehardway.org>

Tested with Python 3.3.6
"""

# A function that prints the value of two (int) variables.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {0} cheeses!".format(cheese_count))
    print("You have {0} boxes of crackers!".format( boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Passes in two integers as the params for the cheese_and_crackers function.
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# passes in two integer variables as the params for the function.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Ultimately passes in two values (10+20 = 30 and 5+6 = 11)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Same deal as the above integer addition using already defined values. (10+100 = 110 and 50+1000 = 1050)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

########## Additional Information ###########
"""
"""
