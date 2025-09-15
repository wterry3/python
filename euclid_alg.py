def gcd(a, b):
# defining a new function called gcd that takes two integer inputs a,b
    while b!= 0:
# starts the while loop. The argument in the loop iterates until the condition becomes false,
# i.e. until the "b" slot satisfies b == 0.
        (a, b) = (b, a%b)
# here we put into "slot 1" the argument from "slot 2", and put into "slot 2" the argument
# "arg slot 1 % arg slot 2".
# In the while loop, this redefinition continues until the argument in "slot 2" is zero.
    return abs(a)
# Once the while loop terminates, i.e. when the argument in slot 2 is zero, the
# argument in slot 1 is the gcd. This returns the absolute value of that number.

# import math
# brings in different math functions in python, in particular the floor function
# commented out, no longer using floor function


while True:
# opens a while loop, apparently with no condition.
    try:
        a = int( input("Enter the first integer: ") )
        break
# this tests converting the string "a" to an integer. If it works, the while loop ends
# at break. If it fails, go to except.
    except ValueError:
        print("Please enter a valid integer.")
# if trying to make "a" an integer fails, ask the user enter an integer and returns to
# the input function.

while True:
    try:
        b = int( input("Enter the second integer: ") )
        break
    except ValueError:
        print("Please enter a valid integer.")
# same thing as "a", for the second integer.

print("GCD of {} and {} is {}".format(a, b, gcd(a, b)))
# calls the function gcd for the integer values of the entered strings a, b. Then,
# prints the result of the function gcd.
