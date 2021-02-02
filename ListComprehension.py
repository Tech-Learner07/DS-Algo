'''
Question:
Write code to find all the digits in a string,
and find the right most digit in the string.

Key:
You must know about list comprehension.
For more details check out here: https://www.programiz.com/python-programming/list-comprehension

Solution:
'''


def digits(string):
    # In list comprehension you can write the code in only on line.
    # Step 1: expression here char
    # Step 2: iteration
    # Step 3: filtering.
    # Eg: [expression(i) for i in list if filter(i)]
    # here [-1] is used to identify the right most digit in the string.
    return [char for char in string if char.isdigit()][-1]


print(digits('Buy 2 Get 1 Free'))
