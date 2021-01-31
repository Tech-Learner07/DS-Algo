'''
Question:
Write a function that combines two list.

Eg:
Given lists:
['one', 'two', 'three', 'four'] and [1, 2, 3, 4]
You have to combine theses lists to look
like this --> [('one', 1), ('two', 2),('three',3)...etc]

Key:
To combine these lists you can use pythons built in
zip function.

Solution:
'''

list1 = ['one', 'two', 'three', 'four']
list2 = [1, 2, 3, 4]

combinedList = []

for tree in zip(list1, list2):
    combinedList.append(tree)

print(combinedList)
