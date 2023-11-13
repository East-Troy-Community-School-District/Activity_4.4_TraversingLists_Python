'''
For Indexes Total
Pawelski
11/12/2022
Introduction to Computer Science

Instructions:
Run the program in debugging mode to see
how it works. Once you understand how the
program works, modify it by adding the following
elements to the list: 5, 2, 8, 3. Does the
program produce the correct output? How can
you avoid this issue?
How could you write line 20 differently?
'''

numbers = [5, 1, 7, 2, 8, 2, 3, 5, 9]
total = 0
for i in range(0, 9):
    total += numbers[i]
print("Total: " + str(total))