# Lab #1, Example #2
# mysecondprogram.py
# Prof. Prud'hommeaux

# NOTE:
# To run this program in IDLE, go up to the Run menu
# and select "Run module"
# Then look in the IDLE Shell window to see what happens.



# Here is some simple variable assignment.
a = 3
b = "The area of a square whose sides are length"

# Here is how you can do some math with variables.
# Python knows a is a numbers because it is not in quotes.
# Python knows a is an integer because is does not have a decimal point.
# The result, c, will also be an integer because a is an integers.
c = a*a

# We can check to make sure like this:
print(type(a))
print(type(c))

# The variable b, on the other hand, is a string! We know because
# it has quotes around it, but we can also check, like this:
print(type(b))


# Even though a and c are integers, Python will let you print them out
# the same way it prints out strings.
print(b, a, "is", c)

# Warning: Python isn't always so nice, as we'll see in Example #3. :)
