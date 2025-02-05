#compare if 2 is NOT equal to 3 using the not equal operator
print(2!=3) 

if 2!=3:
    print("2 is equal to 3")
else:
    ("2 is not equal to 3")

print("Brian" < "John")

# if statement
sales_target = 350
sales_made = 350
#comparing the sales
if sales_made > sales_target:
    print("Target Achieved")
elif sales_made < sales_target:
    print("Target not Achieved")
else:
    print("Target also achieved")


prices = [99,150,1000,4502,300,650,180]
print(prices[0] > 10)

#For loops syntax
#for loops: for each value in sequence perform an action
for i in prices:
    print(i)

#conditional statements in for loops
for price in prices:
    if price < 10:
        print("Less than 10")
    elif price<100:
        print("less than 100")
    elif price<500:
        print("less than 500")
    else:
        print(price)

## loop through a dict (Assignment) 05/02/2025
#Assighnment 1, looping through a dictionary
# Define a dictionary
students_dict = {
    "Kai": 100,
    "Jemmimah": 201,
    "Allela": 304,
    "Mary": 407,
    "Peter": 595
}

# Loop through the dictionary (keys and values)
for key, value in students_dict.items():
    print(f"Student: {key}, Cost in Fare: {value}")


#range
for i in range(1,6):
    print(i)

#Building a counter
attendace = 0
for i in range (1,20):
    attendace += 1
    
print(attendace)


# Assignment2: write a while loop and give reasons why, and breaking a loop

"""
While loops are used when you need to repeat a block of code until a specific condition is met. 
They are ideal for scenarios where the number of iterations is unknown, or the loop should run indefinitely until manually stopped.
"""
# while loop using break
x = 2
while x < 10:
  print(x)
  if x == 3: #here when the iteration reaches a point when x=3 then break and stop the code even if the condition is true
    break
  x += 1

#while loop using continue
x = 2
while x < 10:
  x += 1
  if x == 3: #using continue statement, stop the current iteration then continue
    continue
  print(x)


#while loop
stock = 10
number_of_purchases = 0
while number_of_purchases < stock:
    number_of_purchases +=1 #increment stock
    print(stock - number_of_purchases)

#Building a looping work flow
class1 = ["Ryan", "Reagan", "Ruri", "Nathan"]
if "John" not in class1:
    print("John is not in class")

#create a while loop using or and 
#Building a looping work flow
class1 = ["Ryan", "Reagan", "Ruri", "Nathan"]
class2 = ["John", "Brian", "James"]
if "Ryan" in class1 and "Ryan" in class2:
    print("Ryan is in class")
else:
    print("Ryan is not in both classes")


#Building a looping work flow
class_1 = ["Ryan", "Reagan", "Ruri", "Nathan"]
class_2 = ["John", "Brian", "James"]
if "Reagan" in class_1 or "Reagan" in class_2:
    print ("Reagan is in class")
else:
    print("Reagan is not in any class")

#create a while loop that creates a decrementing loop
# Starting from 10 and decrementing by 1 until it reaches 0
count = 10

while count > 0:
    print(count)
    count -= 1  # Decrease count by 1

print("Loop finished!")


products = []
product_dict = {"Toothpaste" : 10,
                 "Sugar" : 201,
                 "Flour" : 304,
                 "soap" : 407,
                 "Vegetables" : 595,
                 "Cooking oil": 490}

for key,val in product_dict.items(): 
    if val >= 20:
        products.append(key)
print(products)


# look into .zip and .enumerate methods

#using a zip() method in tuples
'''
The zip() function returns a zip object, 
which is an iterator of tuples where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.
'''
class_1 = ("Ryan", "Reagan", "Ruri", "Nathan")
class_2 = ("John", "Brian", "James", "Beth")
x = zip(class_1,class_2) #returns a zip object
print(tuple(x))


#using enumerate methods
class_1 = ("Ryan", "Reagan", "Ruri", "Nathan")
y = enumerate(class_1) #The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.

print(list(y))