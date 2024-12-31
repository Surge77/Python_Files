"""
A program to calculate the total bill and the percentage of tip and dividing it among people 

"""

print("Welcome to tip calculator!\n")

total_bill = float(input("What is the total bill? $"))

print("\n") #adds a new line

tip = int(input("What percentage of tip would you like to give? 10, 12 or 15? "))

print("\n")

tip_percent = tip/100
tip_amount = total_bill*tip_percent

final_bill = total_bill + tip_amount

no_of_people = float(input("How many people to split the bill? "))

split_bill = float(final_bill/no_of_people)

final_amount = round(split_bill, 2) #this is the function used to round off float values here we want two values after point so 2 is written
final_amount = "{:.2f}".format(split_bill) #here we used this formatting method to add accurate two decimal digits after point even 0

print(f"Each person should pay ${final_amount} ") #here concept of fstring is used to print string values

