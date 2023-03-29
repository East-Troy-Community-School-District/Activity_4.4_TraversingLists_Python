'''
While Count
Pawelski
3/28/2023
Python II

Instructions:
Run the program in debugging mode to see how it works.
Modify the program so that it counts the word "yes"
in the list.
'''

words = ["help", "no", "yes", "help", "darn", "yes", "no", "yes"]
index = 0
count_help = 0
while index < len(words):
    if words[index] == "help":
        count_help += 1
    index += 1
print("The word \"help\" appears " + str(count_help) + " times.")