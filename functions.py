def my_name(): #defining the function
    print("This is John learning functions in python")
my_name() #calling the function

"""
A function can have multiple arguments after the function name,
should be placed inside the brackets and should be separated by a comma.
"""
def my_students(student_name, student_age): #The student_name is the argument of the function.
  print("This is " + student_name + " learning Data Science at Zindua School, at the age of " + student_age)

#value sent to the function us known as the argument
#my_students("John", "24") #John and 24 are the arguments in this case
#my_students("Nathan", "35")
#my_students("Ryan", "27")
students = my_students("John", "24")

print(students)

"""
If you not sure of how many arguments to pass to a function, 
you can add * before the parameter name
"""
def DS_students(*students):
  print("The Zindua DS Student that comes from Juja is " + students[0])

DS_students("John", "Ryan", "Gichia")


def DS_students (student1, student2, student3): #sending arguments with the key = value syntax.
  print("The Zindua DS Student that comes from Juja is " + student1)

DS_students(student2 = "John", student1 = "Ryan", student3 = "Gichia")#The order of the arguments does not matter.

"""
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: 
** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""
def DS_students(**student):
  print("The Zindua DS Student that comes from Juja is " + student["student3"])

DS_students(student2 = "John", student1 = "Ryan", student3 = "Gichia")


def DS_students(Town = "Juja"): #using a default parameter
  print("I am a Zindua student and I am from " + Town)

DS_students("Tatu City")
DS_students("Kasarani")
DS_students()
DS_students("Dagoretti")

def zindua_students(students):
  for i in students:
    print(i)

#sending a List as an argument, it will still be a List when it reaches the function:
DS_students = ["John", "Ryan", "Gichia", "Nathan", "Reagan", "Beth"] 

zindua_students(DS_students)

#To let a function return a value use the return statement
def num(i): 
  return i**3 #The values of i should be raised to 3

numbers = num(3)
print(numbers)


#A recursion function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


def square_num(x):
    new_value = x**2 +2*x +4
    print(new_value)
square_num(4)


