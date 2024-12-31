"""
Write a program to calculate the body mass index(BMI) from the users height and weight

BMI is calculated by diving the person's weight in kg by the square of the height in m 
"""

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = (weight) / (height**2)  # or we can write height*height

print("Your BMI is ",BMI ,"kg/m2") 
BMI_as_whole_num = round(BMI) #prints BMI as whole number
#here we used round function to round off the float value

print("BMI as whole number is ", BMI_as_whole_num) #printing as whole number

