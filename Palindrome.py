
def isPalindrome(word):
  word = word.lower() # OR you can use word.upper() it doesn't matter
  
  return word == word[::-1] # [::-1] is the method to reverse a list or a word

isPalindrome(LevEl) # returns True
isPalindrome(malayalam) # returns True
isPalindrome(python) # returns False
