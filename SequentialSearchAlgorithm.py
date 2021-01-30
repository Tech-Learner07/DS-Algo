
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
