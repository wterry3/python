print("Please enter your name:")
# print("") prints the string within ""
name = input()
# input() is a function that prompts the user for a string, stored in the variable "name"
print("Hello, " + name + ".")
# the + concatenates strings together to print

x = sorted(name, reverse=True)
# sorted(name) gives an array sorting the letters alphabetically, [B, i, l, l].
# reverse=True instead sorts the letters in the string "name" in reverse order
string = "".join(x)
# since x is an array, the elements need to be joined to be printed as wanted. Just doing
# str(x) will print the array as a string, i.e. [l, l, i, B]
print("This is your name in reverse: " + string + ".")
# prints the reversed name.
