"""
program to caculate the average student height

"""

student_heights = input("Input a list of student heights ").split()#split a string into a list of substrings

for n in range(0,len(student_heights)): #THIS IS A FOR LOOP USING range() function
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights: #for loop for the sum of the heights
    total_height+= height
print(total_height)

total_students = 0
for students in student_heights: #for loop for the total number of items in the list
    total_students += 1
print(total_students)

average_height = round(total_height/total_students) #we used round function to round off the decimal valule

print(average_height)
