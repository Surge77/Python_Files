"""
A prime number is a number which is only divisible by 1 and itself
0 and 1 are not prime numbers 
The smallest prime number is 2

You need to write a function that checks whether if the number passed into it is a 
prime number or not

eg: 2 is prime number because its only divisible by 1 and 2
But 4 is not a prime number because you can divide it bt 1,2,4

"""
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        number % i ==0
        is_prime = False
    if is_prime:
        print("It is a prime number. ")
    else:
        print("It is not a prime number.")

n = int(input("Check this number: "))

result = prime_checker(number=n)

print(result)

