'''
Find the duplicates in a set.
'''


def duplicate(theList):
    dup = []
    theSet = set()
    for item in theList:
        lengthBefore = len(theSet)
        theSet.add(item)
        lengthAfter = len(theSet)
        if lengthAfter == lengthBefore:
            dup.append(item)
    return dup


aList = ['John Doe', 'Bob', 'Nick', 'John Doe', 'Sue']
duplicates = duplicate(aList)
print(duplicates)
