#compare if 2 is equal to 3
print(2!=3)

if 2!=3:
    print("2 is equal to 3")
else:
    ("2 is not equal to 3")

print("Brian" < "John")

# an if statement
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

#range
'''for i in range(1,6):
    print(i)
'''
#building a counter
attendace = 5
for i in range (1,20):
    attendace += 1
    
print(attendace)

#write a while loop in the assignment2 and reasons why, breaking a loop
#while loop
stock = 10
number_of_purchases = 0
while number_of_purchases < stock:
    number_of_purchases +=1 #increment stock
    print(stock - number_of_purchases)

#Building a looping work flow
class1 = ["Ryan", "Reagan", "Ruri", "Nathan"]
class2 = ["John", "Brian", "James"]
if "John" not in class1:
    print("John is not in names")
if "Ryan" in class1 and class2:
    print("Ryan is in class")
if "Reagan" in class1 or class2:
    ("print Reagan is in class")

#create a while loop using or and 
#create a while loop that creates a decrementing loop

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

##loop through a dict
 