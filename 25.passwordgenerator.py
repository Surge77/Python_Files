"""
Write a program to generate random passowrds

--In Python, random.choice() is a function provided by the random module. It is used to randomly select an item from a sequence, such as a list or a tuple. 
The function takes a sequence as an argument and returns a randomly chosen element from that sequence.

--The random.shuffle() function in Python is used to shuffle the elements of a sequence randomly. 
It operates in place, meaning that it modifies the original sequence directly without returning a new sequence. The function is part of the random module.

"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level  # In this method there is a definite pattern i.e after letters the symbols then numbers hence easy to crack so in hard level everything is shuffled

# password = ""

# for char in range(1, nr_letters +1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(numbers)

# for char in range(1,nr_numbers+1):
#     password += random.choice(symbols)

# print(password)

#Hard level

password_list = [] #we defined an empty listf

for char in range(1, nr_letters +1):
    password_list.append( random.choice(letters)) #here we can also use append used to add element to list

for char in range(1, nr_symbols + 1):
    password_list += random.choice(numbers)

for char in range(1,nr_numbers+1):
    password_list += random.choice(symbols)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list: # for every char in password_list we keep adding every char to password
    password += char

print(password)


