# Lab #1, Example #3
# mythirdprogram.py
# Prof. Prud'hommeaux

# NOTE:
# To run this program in IDLE, go up to the Run menu
# and select "Run module"
# Then look in the IDLE Shell window to see what happens.

# Here is how you can get input from the user!
# When you run this program, over in the IDLE shell,
# it will ask you to enter responses to the questions.

a=input("Enter the length of one side of the rectangle: ")
b=input("Enter the length of the other side of the rectangle: ")

# The variables a and b will store the input that you will enter!

# You can check to make sure it works like this.
print("Your rectangle has sides of length", a, "and", b)

# Now let's print out the perimeter of the rectangle
c = a + a + b + b
print("The perimeter of your rectangle is: ", c)

# Go run the program and see what happens.

#  ... waiting ...

# You saw that c was the actual perimeter. Why?
# a and b are strings, not integers!
# Using + just concatenates them!

# We can check to what type a and b are like this:
print(type(a))
print(type(b))

# You can turn a string into an int like this:
newa = int(a)
newb = int(b)

# Now it's your turn!

# First: check the types of newa and newb.

# Second: create newc, which will be the perimeter.

# Now print out the perimeter of the rectangle!

