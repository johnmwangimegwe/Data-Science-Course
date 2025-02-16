#importing the re library for handling Regular Expressions
import re

""" 
A regular expression (regex) is a sequence of characters that defines a search pattern. 
It is used for pattern matching and text processing in strings.
"""
# A regular expression to find all matches of a pattern
#syntax: re.findall(regexpression,string)
#The regular expression is the pattern we are looking for in a string

movie_instances = re.findall(r"#movies", "I love watching action #movies. I really enjoyed watching the old Guard #movies")
print(movie_instances)
print(type(movie_instances))

# .split()
#A regular expression that splits a string at each pattern match
# syntax: re.split (regexpression(pattern), string)
my_words = "Nice place to chill! I really enjoyed the movies! I can not wait to be back1"
split = re.split(r"!", my_words)
print(split)

#Aregular expression to replace one or many pattern matches with a string
# syntax: re.sub(regexpression(pattern)), new/replacement, string)
my_sentence = "I really like the blue colour. I am thinking of getting a darkblue Ducati"
print(re.sub(r"blue", "Red", my_sentence))

#Supported Metacharacters
#A regular Expression to find a word "user" followed by a digit
#syntax: re.findall(regexpression/pattern, string)

winners = "The winners of this challenge are User1, User 2, User3, User 4 and UserK"
print(re.findall(r"User\s\d", winners)) #\s = white space, \d = digit
print(re.findall(r"User\d", winners))
print(re.findall(r"User\D", winners))#\D not digit character