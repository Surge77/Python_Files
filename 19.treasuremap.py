"""
Write a program which will mark a spot with an X

The map is made up of 3 rows and blank squares

Your program should allow you to enter the position of the treasure using a two-digit system.
the first digit is the horizontal column number and the second digit is the vertical row number

"""

row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]

map_ = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map_[vertical-1]
selected_row[horizontal -1] =  " X "

print(f"{row1}\n{row2}\n{row3}")
