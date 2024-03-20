# Import the sys library
import sys

# Print a greeting to the console
print("Hello, World!")

# Ask the user for their name
Name = input("\nWhat is your name?\nMy name is ")
# Print a greeting using the entered name
print("\nHello, " + Name + "!")
# Print a greeting using string formatting
print("\nHello, {}!".format(Name))

# Print the size of various data types
print("\nData types:")
print("Size int = {}".format(str(sys.getsizeof(int()))))
print("Size float = {}".format(str(sys.getsizeof(float()))))
print("Size complex = {}".format(str(sys.getsizeof(complex()))))
print("Size str = {}".format(str(sys.getsizeof(str()))))
print("Size list = {}".format(str(sys.getsizeof(list()))))
print("Size tuple = {}".format(str(sys.getsizeof(tuple()))))
print("Size range = {}".format(str(sys.getsizeof(range(100)))))
print("Size dict = {}".format(str(sys.getsizeof(dict()))))
print("Size bool = {}".format(str(sys.getsizeof(bool()))))
print("Size set = {}".format(str(sys.getsizeof(set()))))
print("Size frozenset = {}".format(str(sys.getsizeof(frozenset()))))

# Declare a variable number and assign it the value 3.14
number = 3.14
# Print the value of the variable
print("First \"number\" = " + str(number))
# Stop the program's execution to interact with the code
breakpoint()
'''
Example:
number = 
continue or c 
'''
# Print the value of the variable after the breakpoint
print("Another \"number\" = " + str(number))
# Print the value of the variable after the breakpoint
print("Another \"number\" = {}".format(number))
# Print the value of the variable using an f-string
print(f"Another \"number\" = {number}")
