import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) #re.search() finds a match, it returns a match object instead of None.
print(x)