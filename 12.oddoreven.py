"""
Write a program that works out whether given number is even or odd
even numbers can be divided by 2 with no remainder
odd number leave a remainder
"""

num = int(input("Enter a number: "))

if num%2==0: #modulo %   
    print("It is a even number")

else:
    print("It is a odd number")

