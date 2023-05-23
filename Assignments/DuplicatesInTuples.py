'''
Write a Python program to find repeated items in a tuple.
'''


sample_tupl = ('A','B','C','D','E','A','F','B')
duplicates_tup = ()
unique_sample_tupl = ()
for i in sample_tupl:
    if i not in unique_sample_tupl:
        unique_sample_tupl+=(i,)
    else:
        duplicates_tup+=(i,)

print("Input Tuple: ", sample_tupl)
print("Unique Elements in Tuples: ", unique_sample_tupl)
print("Duplicated Items in Tuples: ", duplicates_tup)