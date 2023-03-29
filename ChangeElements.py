'''
Change Elements
Pawelski
3/28/2023
Python II

Instructions:
This program should replace all the "heads" with "tails".
Run the program. Currently, it does not work! Run the
program in debugging mode to see how it works. What is
wrong with the program and how could you fix it?
'''

flips = ["heads", "heads", "tails", "heads", "tails", "tails", "heads"]
for word in words:
    if word == "heads":
        word = "tails"
print(flips)