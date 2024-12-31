"""

To build an automatic pizza order program
-small pizza : $15
-medium pizza: $20
-large pizza: $25

pepperoni for small pizza: $2
pepperoni for medium or large pizzaL $3

extra cheese for any size pizza : $1


"""
print("\n")
print("Welcome to Pizza deliveries!\n")

size = input("What size pizza do you want?S,M,L  ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0 #variable for final bill

if size=="S":
    bill += 15  #bill for small pizza

elif size=="M":
    bill += 20  #bill for medium pizza

else:
    bill +=25 #bill increase for large pizza

if add_pepperoni=="Y":  
    if size=="S":
        bill +=2 # +=added and assigned back the result

if add_pepperoni =="M" or "L":  # Here we used the logical operator or
    bill +=3 

if extra_cheese =="Y":
    bill += 1

print(f"Your total bill is ${bill}") #printing the total bill using fstring concept

#This is a simple program so its not programmed for each and every detail just the conditions required for true statement are being written in conditinals







