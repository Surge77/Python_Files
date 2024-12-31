"""
in the starting code,you'll find the solution from the leap year challenge.First convert
this function is_leap() so that instead of printing "Leap year" or "not leap year" it should return
true if it is a leap year and return false if it is not a leap year

you are then going to create a function called days_in_month() which will take a year and a month
as inputs,

eg: days_in_month(year=2022,month=2)

and it will use this information to work out the number of days in the month then return that as output

eg: 28

the list month_days contains the number of days ina month from january to december for a non-leap year.A leap year 
has 29 days in february
"""

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True 
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  if month > 12 or month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) and month == 2: # Here if only when the condition is true then the below statement executes
    return 29 
  return month_days(month -1)
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












