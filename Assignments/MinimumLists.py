'''
Write a function "minout(l)" that takes a list l of distinct natural numbers (i.e. integers 
from the set {0,1,2,...}) and returns the smallest natural number not present in l. In other 
words, if 0 is not in l, then "minout(l)" returns 0, else if 0 is in l but 1 is not in l, them 
"minout(l)" returns 1, etc. 
'''

def minout(l):
  for i in range(1, len(l) + 1):
    if i not in l:
      return i
  return len(l) + 1

chc = int(input("Enter the size of the list: "))
lst = []
for i in range(chc):
  a = int(input("Enter Element " + str(i + 1) + " : "))
  lst.append(a)

print(lst)
num = minout(lst)
if num:
  print(num)
else:
  print("ERROR!!")
