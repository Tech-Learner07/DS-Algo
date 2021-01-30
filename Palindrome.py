'''
Question:
check whether the given word is a palindrome.

Key:
Palindrome is a sequence that reads the same backwards as forwards
to check that we need to reverse the given string for that we can
use givenWord[::-1].

Solution:
'''
def isPalindrome(word):
  word = word.lower() # OR you can use word.upper() it doesn't matter
  
  return word == word[::-1] # [::-1] is the method to reverse a list or a word

isPalindrome("Level") # returns True
isPalindrome("malayalam") # returns True
isPalindrome("python") # returns False
