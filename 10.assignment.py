"""
 -Create two variables one with your name and other with your age
 - create a function which prints your data as one string
 -create a function which prints any data(two arguments)as one string
 -create a function which calculated and returns the number of decades you already lived foreg 23 (2 decades)

"""
name = input("Enter your name: ") #input for name
age = input("Enter your age: ")  #input for age

def info(n,a): #function for printing data as one string
    print(f"Your name is {n} and ur {a} years old")

info(name,age)

def decades_lived(a): #function for calculating decades lived by passing age through function
    calc_deacades = a/10
    print("You lived ",calc_deacades,"decades")

decades_lived(int(age)) #here we converted string to int
