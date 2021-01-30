'''
name formed by rearranging the letters of another, 
such as listen, formed from silent.

Question:
Check whether two words are anagram.

Solution:
'''

def isAnagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()

    return sorted(w1) == sorted(w2)


isAnagram('Listen', 'Silent') # returns True
isAnagram('python', 'javascript') # returns False
