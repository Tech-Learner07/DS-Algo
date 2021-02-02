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
    return [char for char in string if char.isdigit()][-1]


print(digits('Buy 2 Get 1 Free'))
