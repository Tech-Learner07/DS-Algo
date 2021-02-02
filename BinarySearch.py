'''
Check it out: https://en.wikipedia.org/wiki/Binary_search_algorithm
'''


def binarySearch(theList, target):
    first = 0
    last = len(theList)-1
    isThere = False
    while first <= last and not isThere:
        mid = (first+last)//2
        if theList[mid] == target:
            isThere = True
        else:
            if target < theList[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return isThere


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
          11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
target = 16
if binarySearch(myList, 16):
    print('Item found.')
else:
    print('Item not found.')
