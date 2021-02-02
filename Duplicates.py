'''
Find the duplicates in a set.

Key:
Identifying the use of set() function
'''


def duplicate(theList):
    # Empty list to add duplicates
    dup = []
    # Empty set for to check for duplicates
    theSet = set()
    for item in theList:
        # Get the length of the set
        lengthBefore = len(theSet)
        # Attempt to add item to the set
        theSet.add(item)
        # Check the new length of the set
        # Duplicates cannot be add to a set
        lengthAfter = len(theSet)

        # If the length doesn't changed the item is a duplicate
        if lengthAfter == lengthBefore:
            dup.append(item)
    return dup


aList = ['John Doe', 'Bob', 'Nick', 'John Doe', 'Sue']
duplicates = duplicate(aList)
print(duplicates)
