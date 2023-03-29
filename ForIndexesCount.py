'''
For Indexes Count
Pawelski
3/28/2023
Python II

Instructions:
Run the program in debugging mode to see how it works.
Modify the program so that it counts the word "yes"
in the list.
'''

words = ["help", "no", "yes", "help", "darn", "yes", "no", "yes"]
count = 0
for i in range(0, len(words)):
    if words[i] == "help":
        count += 1
print("The word \"help\" appears " + str(count) + " times.")