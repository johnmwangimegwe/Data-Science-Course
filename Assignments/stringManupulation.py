#Types of inbuilt functions for strings

my_name = "John-Terry"
print(len(my_name))

#Indexing
print(my_name[2:5])
print(my_name[-5:-1])
print(my_name[0:5:2]) #index but skiping 2 characters from index o to 5 it is also known as striding
print(my_name[::-1]) #reverse string
print(my_name[-5:])


#Strides
my_surname = "MwangiMegwe"
print(my_surname[0:6:1])

#Splitting a string
students = "Brayan, Bethany, John, Nathan, Reagan, Ryan"
text = "johnmwangi@jkuat.com"
text2 = "My name is John Mwangi a DS Student"

#use the .split() method to split a string and return a splitted value as a list
students_list = students.split(sep=",", maxsplit=2)
print(students_list)
print(text.split("@"))
print(text2.split(" ", maxsplit=2))

#split a string starting from the left
students_left = students.rsplit(",", maxsplit=2)
print(students_left)


#Escape sequence
#We can escape a sequence of characters in a string using backslash \n and \r.
#\n - NEW LINE
#\r - CARRIAGE RETURN

sentence1 = "I am a lecturer at JKUAT\n and a student at University of Nairobi"
sentence2 = "I am a lecturer at JKUAT and a student at \r University of Nairobi"
print(sentence1)
print(sentence2)

print("---------------")

sentence3 = "I am a student at Zindua scho\r ol"
print(sentence3)

#Joining strings
# we use the .join() to join diff strings
# syntax: separator.join(iterable)
my_list = ["I", "am", "a", "students", "at", "zindua", "school"]
print(" " . join(my_list))



#Types of In-built functions for strings

# .lower() - Converts all characters in a string to lowercase
# .upper() - Converts all characters in a string to uppercase

my_name = 'Ruth-Mwaura'
print(len(my_name))

# Indexing 
print(my_name[4])

print(my_name[0:5])

print(my_name[::-1])  # Reversing a string

print(my_name[-6:])

# Strides 

my_surname = "mwanyumba"
print(my_surname[0 : 6 : 1])

#Splittung a string 

students = "My name is Brayan Kai Mwanyumba"

# We use the .split() method to split a string and return the splitted values as a list
students_list = students.split(sep=" ", maxsplit=1)
print(students_list)

# Split a string starting from the right
students_left = students.rsplit(sep=" ", maxsplit=1)
print(students_left)

print("------------------------------------")

# Escape Sequence
# We can escape a sequence of characters in a string using \n and \r 
# \n - New line
# \r - Carriage return 

sentence1 = "I am a teacher at\n University of Nairobi\n I teach Chemical Engineering"
print(sentence1)

print("------------------------------------")

sentence2 = "I am a teacher at\r University of Nairobi\r I teach Chemical Engineering"
print(sentence2)

print("------------------------------------")

sentence3 = "I am a student at\r Zindua School"
print(sentence3)

print("------------------------------------")

# JOINING Strings 
# We use the .join() method to join strings
# Syntax: separator.join(iterable)

my_list = ["Brayan", "Kai", "Mwanyumba"]
print(" ".join(my_list))

print("------------------------------------")

# Stripping Characters from a string
# We use the .strip() method to remove characters from a string
# Syntax: string.strip(characters)

sentence4 = "I am a student at Zindua school am"
print(sentence4.strip("I am student"))

print("*******************************************")

# Assignmenmt
# 1. Understand the logic between the .split() and .rsplit() methods
# 2. Look into the \r escape sequence and understand how it works with code examples
# 3. Try and see if the issues we faced with \r and .split() are re;lated to python versions 
# 4. Look into Finding and Replacing Strings 
#       - Use the .find() method to find a string in a string
#       - Use the .index() method to find a string in a string
#            - Implement try and accept clause to handle value error when you dont find the string
# 5. Use .count() method to count the number of times a substring appears in a string 
# 6. Use the .replace() method to replace a substring in a string with another substring


# 1. Understand the logic between the .split() and .rsplit() methods
""" The split() method splits a string into a list."""
students = "Brayan, Bethany, John, Nathan, Reagan, Ryan"
text1 = "johnmwangi@jkuat.com"
text2 = "My name is John Mwangi a DS Student"

#use the .split() method to split a string and return a splitted value as a list
students_list = students.split(sep=",", maxsplit=2)
print(students_list)
print(text1.split("@"))
print(text2.split(" ", maxsplit=2))

#split a string starting from the left
students_left = students.rsplit(",", maxsplit=2)
print(students_left)

print("---------------")

# 2. Look into the \r escape sequence and understand how it works with code examples
"""
The Carriage Return (\r):

The \r character is a special character that moves the cursor back to the beginning of the current line without advancing to the next line.
When the print function encounters \r, it moves the cursor to the start of the line, and any text after \r will overwrite the text that was previously on that line.

"""
#Example using \r - CARRIAGE RETURN

sentence1 = "I am a lecturer at JKUAT\n and a student at University of Nairobi"
sentence2 = "I am a lecturer at JKUAT and a student at \r University of Nairobi"
print(sentence1)
print(sentence2)

sentence3 = "I am a student \r at Zindua \r school"
print(sentence3)

print("---------------")

# 3. Try and see if the issues we faced with \r and .split() are related to python versions 
"""
What Does strip() Do?
The strip() method is used to remove leading and trailing characters from a string.

It removes all combinations of the specified characters from the beginning and end of the string.

It does not remove characters from the middle of the string.

"""
sentence4 = "I AM A STUDENT AT ZINDUA SCHOOL "
print(sentence4.strip("I AM SCHOOL")) #This means the characters to remove are: I, (space), A, M, S, C, H, O, L
print(sentence4.strip("I AM A"))

print("---------------")

# 4. Finding and Replacing Strings

# 4a. Use the .find() method to find a string in a string
sentence = "I am a lecturer at JKAAT and a student at University of Nairobi."
position = sentence.find("lecturer", 0,8)
print(position)
print(f"The word 'lecturer' is found at index: {position}")

# 4b. Use the .index() method to find a string in a string
try:
    index_position = sentence.index("University")
    print(f"The word 'University' is found at index: {index_position}")
except ValueError:
    print("The word 'University' was not found in the string.")

# 4c. Implement try and except clause to handle ValueError when the string is not found
try:
    index_position = sentence.index("JOHN")
    print(f"The word 'JOHN' is found at index: {index_position}")
except ValueError:
    print("The word 'JOHN' was not found in the string.")

print("---------------")

# 5. Use the .count() method to count the number of times a substring appears in a string
text3 = "I am a lecturer at JKUAT main Campus and a student at University of Nairobi in Nairobi Campus."
str_count = text3.count("Nairobi")
print(f"The word 'Nairobi' appears {str_count} times in the text.")

str_count2 = text3.count("Campus")
print(f"The word 'Campus' appears {str_count2} times in the text.")

print("---------------")

# 6. Use the .replace() method to replace a substring in a string with another substring
replace_text = text3.replace("Nairobi", "Kabete")
print("Replaced Text:", replace_text)
