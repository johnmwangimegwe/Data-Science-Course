# Normal Function 
#from math import sqr

def raise_to_power(a,b):
    """Returns the power of a raised to b"""
    power = a ** b
    return power
print(raise_to_power(2,3))

print("-------------------------------------")

# A Lambda Function 
# Syntax: Func_name = lambda arguments/paameters : action
raise_to_power_lambda = lambda num1, num2 : num1 ** num2 
print(raise_to_power_lambda(8,30))

print("-------------------------------------")

# Write a Lambda function to concatenate two strings(Continent and Country) 

# Error handling 

def square_root(a):
    """Returns the square root of a number"""
    return a ** 0.5

print(square_root(-9))

print("-------------------------------------")

#Error Handling with the "try" and "except" clause
#Similar to "break" and "continue" statements in loops

def sqrt(b):
    """Returns the square root of a number
    But if the parameter passed is not a float/integer,
    It will return an error message"""
    try:
        return b ** 0.5
    except:
        print("Input must be an Integer ot float value")
        
print(sqrt(-10000))

print("-------------------------------------")

#Assignment
#Look into Anonymous Functions in respect to using lambda functions 
# Create an Anonymous function using the map()(Built in function) funnction
# Create a try and except clause for a sqaureroot function not to accept negative values  
#Create another try and except clause for when there is an import error in the math module importation 


#1. Using lambda with map() to square a list of numbers
numbers = [-6, -2, 3, 4.2, 5, 10]
squared_numbers = list(map(lambda y: y ** 2, numbers))
""" The map() function takes a list (or any collection of items) and applies a given function to each item in that list, returning the new results."""
print(f"Squared Numbers = {squared_numbers}")


#2. Try-Except Clause for a sqaureroot function not to accept negative values  
import math

def square_root2(numbers):
    """
    Returns the square root of a given number.
    If the number is negative, it raises an error and returns an appropriate message.
    """
    try:
        if numbers < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        return math.sqrt(numbers)
    except ValueError as e:  # Catch the ValueError exception
        return str(e)  # Convert the error message to a string and return it

# Testing with a negative number
print(square_root2(-24))  
print(square_root2(25))  


# 3. Try and Except clause for handling import errors
try:
    import math  # Try importing the math module
except ImportError:
    print("Error: The 'math' module could not be imported.")

# If successful, use the module
print(math.sqrt(16))  # Testing the math module

try:
    import John_module  # This module does not exist
except ImportError:
    print("ImportError: The module above could not be imported.")
