'''
Intersection of 2 lists is the elements which are common to both the lists
ie. list1 = [1,3,5,7]
    list2 = [1,2,3,4]
    intersection of lists1 and list2 is [1,3]
'''


def intersection(list1, list2):
    list3 = [c for c in list1 if c in list2]
    return list3


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [2, 3, 5, 7, 11, 13, 17, 19]

print(intersection(list1, list2))
