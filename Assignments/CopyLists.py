'''
Write a Python program for Cloning or Copying a list using the slicing technique, method of shallow copy, and deep copy.
'''

import copy

lst1 = [1,2,3,[4,5,6],7]
print(lst1)
lst2 = copy.copy(lst1)
print(lst2)
lst3 = copy.deepcopy(lst1)
print(lst3)