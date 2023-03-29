'''
For Total
Pawelski
3/28/2023
Python II

Instructions:
Run the program in debugging mode to see how it works.
Once you understand how the program works, modify it
by adding the following elements to the list: 5, 2, 8, 3.
Does the program produce the correct output?
How can you avoid this issue?
'''

numbers = [5, 1, 7, 2, 8, 2, 3, 5, 9, 5, 2, 8, 3]
total = 0
for number in numbers:
    total += number
print("Total: " + str(total))