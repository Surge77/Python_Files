"""
Writing a program to check weather eligible to ride a rollercoaster 
the condition is your height needs to be greater than 120cm 
apply if else condition

"""

print("\n")
print("Welome to the Rollescoaster! \n")

user_height = int(input("Enter your height in cm: "))

print("\n")

if user_height>120:
    print("You can ride the rollercoaster! ")
else:
    print("Sorry! You cannot ride the rollercoaster:(")
