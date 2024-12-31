"""
Write a program which will select a random name from a list names.the person 
selected will have to pay for everybodys food bill

imp: You are not allowed to use choice() function 

line 6 splits the string names_string into individual names and puts them inside
a list called names.For this to work you must enter all the names followed by 
comma then space for eg: name, name, name

--Using str.split(',')

we can directly convert it into a list by separating out the commas using str.split(',')

str_inp = "Hello,from,Askpython"
op = str_inp.split(",")
print(op)

output:
['Hello', 'from', 'Askpython']

len() -to get number of characters in a string

"""

import random

names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(",") #this becomes a list now separated by ' ' and ,

#the below method is for understanding the concept of indices in a list

num_items = len(names)#gets the total number of items in the list

random_name = random.randint(0,num_items - 1) # generates a random number

person_who_will_pay = names[random_name]  # will print the name according to the index of list

# person_who_will_pay = random.choice(names) this is with the help of choice function which is much easier with less lines of code

print(person_who_will_pay + " is going to buy the meal today")