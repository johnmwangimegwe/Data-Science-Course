#Assignment  - John
#1. Look into default and Flexible arguments in functions
""""
A default function calls the function without argument, it uses the default value:
"""
def DS_students(Town = "Juja"): #using a default parameter
  print("I am a Zindua student and I am from " + Town)

DS_students("Tatu City")
DS_students("Kasarani")
DS_students()
DS_students("Dagoretti")

#2. In flexible arguments look into *args and **kwargs
"""
If you not sure of how many arguments to pass to a function, 
you can add * before the parameter name, this is known as *args
"""
def DS_students(*students):
  print("The Zindua DS Student that comes from Juja is " + students[0])

DS_students("John", "Ryan", "Ruri")

"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
This is known as **kwargs
"""
def DS_students(**student):
  print("The Zindua DS Student that comes from Juja is " + student["student3"])

DS_students(student2 = "John", student1 = "Ryan", student3 = "Gichia")


#3. Look into Lambda Functions
"""
A lambda function is a small, anonymous function that can have any number of arguments but only one expression.
The syntax is lambda arguments : expression
"""
#The exponential function raises y to power x and adds the product of yx using the lambda function
Exponential_function = lambda x,y: y ** x + y*x
print(Exponential_function(5,6))

#A lambda function using 4 arguments
quadratic_equation = lambda a,b,c,x: a*(x**2) + b*x + c
sum1 = quadratic_equation(2,3,5,-4)
sum2 = quadratic_equation(2,3,5,4)
print([sum1,sum2])

"""
A lambda function can take several arguments but should be in one expression
"""