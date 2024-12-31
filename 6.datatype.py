"""

Write a program that adds the digits in a two digit number if the input is 35 then the output should be 3+5=8

"""
num = input("type a two digit number: ")  # taking a two digit number as input

# print(type(num))  here when we check the type of the data we get as string
# so as we know string can be manipulated through their indexes so we can add them

first_digit = num[0]  # index for first string character
second_digit = num[1]  # index for second string character

result = int(first_digit) + int(
    second_digit
)  # addition of the two characters using their indexes

print(result)  # printing their result
