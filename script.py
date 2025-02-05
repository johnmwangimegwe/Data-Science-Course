# Methods : A function thats only available to a specific data type and in our case we are focusing on strings 

my_uni = "Jomo Kenyatta University of Agriculture and Technology, Main Campus"

print(my_uni)

# Replace Some Words in My String 
# Syntax : .replace(text_to_be_replaced, text_to_change_it_to)

my_uni = my_uni.replace("Main Campus", "Nairobi Campus")

print(my_uni)

# Change the Case of my String 
#Syntax : .upper() or .lower()
print (my_uni.upper()) #uppercase
print(my_uni.lower()) #lower case

my_name = "John"

print(my_name)

my_name_lower = my_name.lower() #Rewriting my name in lower case

print(my_name_lower) 

# Asssignment : Try running other methods on strings and see what they do
print(my_uni.capitalize()) #converts the first character to upper case
print(my_uni.count("campus")) #Returns the number of times a specified value occurs in a string

my_sentence = "I am a data science student at zindua school"

# Multi Line Strings 

my_paragraph = """I am a student at Zindua School 
I am Learning Data Science
I enjoy working with fellow classmates
I always submit my assignments on time"""

print(my_paragraph)

# Lists 
student_names = ["Brayan", "John", "Jane", "Mary", "Peter"]

print(type(student_names))

# Assignment : Try Acessing multiple elemnts in your list, try acessing alternating values in your list
print(student_names[3])
print(student_names[:2])
print(student_names[1:3])


# Dictionaries 
students_name = ["Kai", "Jemmimah", "Allela", "Mary", "Peter"]
student_id = [100, 201, 304, 407, 595]

students_dict = {"Kai" : 100,
                 "Jemmimah" : 201,
                 "Allela" : 304,
                 "Mary" : 407,
                 "Peter" : 595}

print(students_dict["Kai"])#print the val under Kai

print(students_dict.keys()) #print all the keys in dict

# Assignment : try updating a Value , Add a key value pair to the dictionary, duplicate the keys
students_dict["Kai"] = 2000 #changing the val of Kai from 100 to 2000
students_dict["John"] = 300 #adding John to the dict with his val
#duplicating keys and val in the dict is not possible since Dictionary items are ordered, changeable, and do not allow duplicates. 
print(students_dict)


# Sets 

student_colors = {"Blue", "Red", "Green", "Yellow", "Blue"}

# Convert a list into a set
student_name_set = set(students_name)

print(type(student_name_set))

# Tuples 
# They are immutable meaning you cant change add or remove elements from them
# They are ordered
class_locations = ("first floor", "ground floor", "board room")

print(class_locations[0])

# Assigmnet : Write A summary of Data Structures (Lists , Dictionaries, Sets, Tuples). 
# Looking into these aspects; immutability, ordered, Allow duplicates, Syntax, use cases, SubSet them 
"""
Lists: Ordered, mutable, allows duplicates. Syntax: [1, 2, 3]. 
Tuples: Ordered, immutable, allows duplicates. Syntax: (1, 2, 3). 
Sets: Unordered, mutable, no duplicates. Syntax: {1, 2, 3}. 
Dictionaries: ordered, mutable, no duplicate keys. 
Syntax: {"key": "value"}. Use: Key-value mapping.
"""