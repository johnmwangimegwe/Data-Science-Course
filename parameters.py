#Write a function that takes Key word arguments of employee details, containing(name, age , ID, salary).
#Call the funtion for two employees.
def employee_details(**employees):
    print("Employee Details:")
    for key,value in employees.items():
        print(key + ":" + str(value))
    return ""
# Calling the function for two employees
print(employee_details(name = "John", age = 30, ID = "SCG200/2019", salary = 50000))
print(employee_details(name = "Nathan", age = 28, ID = "SCG201/2019", Bonus = 5000))


#A lambda function to concanate 2 strings (continent and country)
strings_function = lambda continent,country: continent + " - " + country
print(strings_function("Africa", "Kenya"))  
print(strings_function("Europe", "Germany"))  


#Error handling
def square_root(a):
    """ Returns the square root of a number"""
    return a**(0.5)
print(square_root(-9))

#Error handling with the "try" and "except" clause
#similar to "break" and "continue" statements in loops
def sqrt(b):
    try:
        return b**0.5
    except TypeError:
        return "Invalid Input. Please enter an interger or float value"
print(sqrt("Tom"))

