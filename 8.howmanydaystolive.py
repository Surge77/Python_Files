"""
Write a program using maths and f-strings that tells us how many days,weeks,months we have left
if we live until the age of 90

it will take current age as input and output the message in this format

"You have X days, Y months , Z years left"
where x,y,z are repaced with actual calculated numbers
1 year = 365 days
1 year = 52 weeks
1 year = 12 months
"""

age = int(input("What is your current age: "))

days = 32850 -(365*age) #32850 is 90*365 here 90 means till the age of 90
weeks = 4680 - (52*age) # 4680 is 90*52
months = 1080 - (12*age) # 1080 is 90*12

print(f"Your have {days} days {weeks} weeks and {months} months left") #here we use the concept of f-string 
# where we write f at the start and write each variable in curly brackets and it automatically converts them to string and prints 

# AN other efficient way of doing this is

age_remaining = 90 - age #here we subtracted the remaining age from beginning itself
days_remain = age_remaining*365
weeks_remain = age_remaining*52
years_remain = age_remaining*12

print(f"You have {days_remain} days , {weeks_remain} weeks and {years_remain} years left")
