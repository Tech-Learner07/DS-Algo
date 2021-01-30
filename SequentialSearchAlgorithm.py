'''
Note:
A sequential search is made over all items one by one. 
Every item is checked and if a match is found then that 
particular item is returned, otherwise the search 
continues till the end of the data collection.

Example:
'''
def seqSearch(numList,n):
  isThere = False
  for i in numList:
    if i == n:
      isThere = True
      break
  
  return isThere

numbers = range(0,101)

seqSearch(numbers,27) # Returns True
seqSearch(numbers,111) # Returns False
