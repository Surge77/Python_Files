"""
Write a program that automatically prints the solution to the fizzbuzz game

your program should print each number from 1 to 100 in turn 

--when the number is divisible by 3 then instead of printing the number it should print "Fizz"

--When the number is divisible by 5,then instead of printing the number it should print "Buzz"

--And if the number is divisible by both 3 and 5 eg: 15 then instead of the number it should print "Fizzbuzz"

"""


for num in range(1 , 101):
    if num % 3 ==0 and num % 5 ==0:
        print("Fizzbuzz")
    elif num % 3 ==0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
        
        
    
