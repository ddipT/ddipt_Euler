"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#Needs far more work to be good, currently just gets list of squares, not the correct challenge
# Testinmg
squares = []
x=1
#Including stuff
while x**2 < 1000:
    squares.append(x**2)
    x+=1

# 36 64 and 900

