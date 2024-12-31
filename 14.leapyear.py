"""
Write a program that works out whether if a given year is leap year.A normal
year has 365 days, leap year have 366, with an extra day in february.


Determining whether a year is a leap year involves checking a few conditions. 

--If the year is evenly divisible by 4, it is a leap year.
For example: 1996, 2004, 2008 are leap years because they are divisible by 4.
--However, if that year is also divisible by 100, it is not a leap year unless...
--The year is divisible by 400. If a year is divisible by 100 but also divisible by 400,then it is a leap year.

"""
year = int(input("Enter the year: "))

if year%4==0:
    print("It is a leap year") #condition for leap year

elif year%100==0 and year%400==0:
    print("It is a leap year") #condition for leap year and logical operator is used here

else:
    print("It is not a leap year") # condition for non leap year


