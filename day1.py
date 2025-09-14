# Day 1: Create a shopping list program that takes input from the user for the number of items they want to buy and their prices.

list_of_items = []
n = int(input("enter the number of items: "))
for i in range(n):
    shopping_list = int(input("enter the each item price: "))
    list_of_items.append(float(shopping_list))
sum = 0
for i in list_of_items:
    sum+=i

if sum >1000:
    discount = sum*0.1
    print("your price after discount is: ",discount)
else:
    print("your total price is: ",shopping_list)
# There is no need to call 'init' from mimetypes or use 'git' here.
# If you want to save your project using git, you can run the following commands in your terminal:
# git add .
# git commit -m "Save project"
# git push;


    
