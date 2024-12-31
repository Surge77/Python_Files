"""
--Problem statements: 
-create a greeting for your program
-ask the user the city they grew up in
-ask the user the name of a pet
-combine the name  of the city and pet and show them their band name
-make sure the input cursor shows at new line


"""
print("Welcome to band name generator")

print("what's the name of city you grew up in? ")
city = input()

print("What's your pet name? ")
pet = input()

print("Your band name could be ", city , pet)

# An alternative method of printing the above things
citys = input("Enter your city you grew up in: \n")
pets = input("Enter your favorite pet: \n")

print("Your band nmae could be "+ citys +" " + pets)