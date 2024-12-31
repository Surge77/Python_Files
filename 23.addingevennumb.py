""" 
Write a program that calculates the sum of all the even numbers from 1 to 100,
including 1 and 100

eg: 2+4+6+8+10+....98+100

there should be only 1 print statement in your console ouptput.
it should just print the final total and not every step of the calculation

hint: there are quite a few ways of solving the problem.
you wll need to use the range() function in any of the solution
"""

sum_of_evens = 0

for num in range(2,101,2): #the third parameter here is the step size
    """
start (2): This is the starting value of the sequence. In this case, the sequence starts with the number 2.

stop (101): This is the end value of the sequence. The sequence goes up to, but does not include, this value. In this case, the sequence stops before reaching 101.

step (2): This is the difference between each pair of consecutive values in the sequence. In this case, the step is 2, meaning that only even numbers will be included in the sequence."""
    sum_of_evens += num


print(sum_of_evens)


#another way of solving

total2 = 0 

for num2 in range(1, 101):
    if num2%2==0:
        total2 += num2

print(total2)
