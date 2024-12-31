"""
Write a program to calculate the body mass index(BMI) from the users height and weight

BMI is calculated by diving the person's weight in kg by the square of the height in m 

we need to use if else conditions this time to tell the interpretation of their bmi
-Uder 18.5 they are underweight
-over 18.5 but below 25 they have a normal weight
-over 25 but below 30 they are overweight
-over 30 but below 35 they are obese 
-above 35 they are clinically obese
"""

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = (weight) / (height**2)  # or we can write height*height

print("Your BMI is ",BMI ,"kg/m2\n") 
BMI_as_whole_num = round(BMI) #prints BMI as whole number
#here we used round function to round off the float value

print("BMI as whole number is ", BMI_as_whole_num) #printing as whole number

print("\n")

if BMI<18.5:                           #In betweeen if else we can put multiple elif statements
    print("You are underweight")

elif 18.5<BMI<25:
    print("You have normal weight")  # Here we can also use only multipleless than elif conditions

elif 25<BMI<30:
    print("You are overweight")

elif 30<BMI<35:
    print("You are obese")

else:
    print("You are clinically obese")
