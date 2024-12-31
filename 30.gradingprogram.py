"""
You have access to a database of student_scores in the format of a dictionary.
the keys in student_scores are the names of the students and their values are their exam scores

write a program that converts their scores to grades.by the end of your program you should have a new dictionary called 
student_grades that should contain student names for keys and their grades for values.the final version of the student_grades dictionary will be checked

the scoring criteria
scores 91 - 100 = outstanding
scores 81 - 90 = exceeds expectations
scores 71 - 80 = acceptable
scores 70 or lower: grade = fail

Here dictionary concept is being used
"""

student_scores = {
    "Harry": 91,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74, 
    "Neville": 62,
}

#creating an empty dictionary called student_grades
student_grades = {}

#adding the grades to the student_grades
for student in student_scores:
    score = student_scores[student]
    if score >90:
        student_grades[student] = "Outstanding"
    elif 90>score>80:
        student_grades[student] = "Exceeds expectations"
    elif 80>score>70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)