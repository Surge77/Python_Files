"""
write a program that calculates the highest score from a list of scores

--meaning of the starting lines of code
input("Input a list of student scores: "): This line prompts the user to input a list of student scores.

.split(): This method is used to split the input string into a list of substrings. By default, it splits the string at whitespace characters (spaces, tabs, and newlines).

The for loop iterates over each element in the list obtained from the input. It converts each element to an integer using int() and updates the list with these integer values.

print(student_scores): This line prints the final list of student scores, where each score is an integer.

here max() and min() functions also can be used but we need to solve this using for loop
max() - generates the maximum number in the list
min() - generates the minumum number in the list
"""

student_scores = input("Input a list of student scores: ").split()
#he user enters a space-separated list of scores, and the code converts them into integers, creating a list of integers.

for n in range(0,len(student_scores)):  #loop for taking the input
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
#in this for loop score is a new variable created to compare
#always create this varible in a singular form of the original varible
for score in student_scores: #loop for finding the highest score
    if score > highest_score:
        highest_score = score
print(f"Your highest score in the class is {highest_score}")
