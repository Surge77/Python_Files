"""
You are going to write a program that tests the compatiblity between 
two people.We're going to the super scientific method recommended by buzzfeed

To work out the love score between two people 

Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number

-the lower() function changes all the letters in a string to lower case
-the count() function will give you the number of times a letter occurs in a string 

-for love score less than 10 or greater than 90 the message should be
"Your score is x, you go together like coke and mentos."

-for love scores between 40 and 50, the message should be
"Your score is y, you are alright together"

-otherwise the message will just be their score e.g:
"Your score is x"
"""
print("\n")
print("Welcome to Love calculator\n")

name1 = input("What is your name: ")
name2 = input("What is her name: ")

combined_string = name1 + name2 #Here we combined the name1 and name2 strings and concatenated them

lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l +o+v+e

love_score = int(str(true) + str(love)) # for the final conditions we needed to convert this whole concatenation to int

# print(f"Your love score is {love_score}")

#These are the onditions for the interpretation of the love score
if (love_score<10) or (love_score>90):
    print(f"Your score is {love_score}, You go together like coke and mentos")

elif love_score>=40 and love_score<= 50:
    print(f"Your score is {love_score}, You are alright together ")

else:
    print(f"Your score is {love_score}")