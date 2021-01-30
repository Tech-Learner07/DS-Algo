'''
Question:
Count how many time each character occurs
in a string.

Key:
iterate through every character in a string.
if this character in the dictionary then 
increment with 1 else set its value to 1.

Solution:
'''

def occur(word):
    counter = {} # dict to store character occurance
    for char in word:
        if char in counter:
            # If the character already is in the dict then increment 1
            counter[char] += 1 
        else:
            # If not then set its value to one
            counter[char] = 1
    
    print(counter)

occur('banana')