"""
We are going to write a program to build a calcualtor based on the concept of functions with outputs

we use return in funtions instead of print because the output can directly be used to pass in other function calls

"""
import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#functions for different operations

#addition
def add(n1,n2):
    return n1 + n2

#subtraction
def subtract(n1,n2):
    return n1 - n2


#multiplication
def multip(n1,n2):
    return n1 * n2

#division
def divide(n1,n2):
    return n1 / n2

#a dictionary where the operators are the keys and function names are the values
operations = {  "+" :  add,
                "-" :  subtract,
                "*" :  multip, 
                "/" :  divide,
            }



def add(n1, n2): #functions for operations
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: ")) # we converted the type to float to avoid errors with decimal numbers
  for symbol in operations:
    print(symbol)
  should_continue = True  # This is known as flags in python or any language
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer # when looping again the previous answer should become num1 and should be further calculated with second number
    else:
      should_continue = False
      os.system("cls") # to clear the screen
      calculator() # this is recursive function i.e function calling itself

calculator()
