'''
Student Scores
Pawelski
11/12/2022
Introduction to Computer Science

Instructions:
This is a complex and large program! Let's look at a section
at a time. First, lines 38 to 46. What does this section of the
program do? If you are not sure, run the program in debugging
mode to see how each line executes. Why did Mr. Pawelski use
parallel lists in this program? How did he populate each?
Add the following two lines of code after this section...
student_names.sort()
scores.sort()

What happens? Are the student's names and scores at the same
index? Based on this, why should we be cautious when working
with parallel lists?


Next, let's look at lines 48 to 53. What does this section of
the program do? How many lists are we traversing?


Next, let's look at lines 55 to 62. What does this section
do? How many lists are we traversing? Why did Mr. Pawelski
need to uses indexes to traverse the parallel lists together?


Finally, let's add the code to find the student with the lowest
score.
'''

student_names = []
scores = []

# Get all the students' scores and store them
repeat = "y"
while repeat == "y":
    student_name = input("Enter the name of a student >> ")
    score = float(input("Enter the score that " + student_name + " got on the test. >> "))
    student_names.append(student_name)
    scores.append(score)
    repeat = input("Do you need to enter another student? (y/n) >> ")
    print()
    
# Find the average of all the scores
total = 0
for score in scores:
    total += score
average = total / len(scores)
print("The average on the test was " + str(average))

# Find the student who got the highest score
highest_score = scores[0]
highest_score_student = student_names[0]
for i in range(0, len(student_names)):
    if scores[i] > highest_score:
        highest_score = scores[i]
        highest_score_student = student_names[i]
print(highest_score_student + " got the highest score.")

# Add your code here!