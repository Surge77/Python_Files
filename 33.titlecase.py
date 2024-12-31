"""
To convert the string to title case using title() function and function with outputs
the title() function converts the string into the standard format 

eg : tEjAs becomes Tejas after using title function

"""

#Function with outputs

def format_name(f_name,l_name):
    first = f_name.title()
    last = l_name.title()
    return f"Your first name is {first} and last name is {last}" #this return acts as print statement which returns output also acts as ending line in function

f = input("Enter your first name: ")
l = input("Enter your last name: ")

result = format_name(f_name=f ,l_name=l)
print(result)