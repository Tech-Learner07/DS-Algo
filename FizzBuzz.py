'''
Question:

Write a program to print numbers from 1 to 100.
For the multiples of 3 print 'Fizz', for the 
multiples of 5 print 'Buzz' and both multiples
3 & 5 print 'FizzBuzz'.

Key:
Knowing the modulo(%) operator that is
if n % 5 == 0
if n % 3 == 0
if n % 3 and n % 5 == 0

Solution:
'''
def fizzBuzz():
  # printing numbers from 1 to 100
  for n in range(1, 101):
    # if number is multiple of 3 and 5
    if n % 3 == n % 5 == 0:
      print("FizzBuzz")
    elif n % 3 == 0:
    # if number is multiple of 3
      print("Fizz")
    elif n % 5 == 0:
    # if number is multiple of 5
      print("Buzz")
    else:
      print(i)

fizzBuzz()
