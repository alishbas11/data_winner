# DAY 1: Conditional Statements and Loops:


# Write a program to calculate the total cost of items in a shopping list. 
# If the total cost exceeds $1000, apply a 10% discount and display the final amount to be paid.


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



    
