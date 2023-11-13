'''
For Count
Pawelski
11/12/2022
Introduction to Computer Science

Instructions:
Run the program in debugging mode to see how it works.
Modify the program so that it counts the word "yes" in the list.
We have now looked at three different ways to traverse a list:
using a while loop, using a for loop with indexes, and using a
for loop. Which version do you prefer? Why? Is one way better
than the others? Why is traversing useful?
'''

words = ["help", "no", "yes", "help", "darn", "yes", "no", "yes"]
count = 0
for word in words:
    if word == "help":
        count += 1
print("The word \"help\" appears " + str(count) + " times.")