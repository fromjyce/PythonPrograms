'''
Write a Python program to sort (both ascending and descending) a list of dictionaries by values using the lambda function.
'''


num_dicts = int(input("Enter the number of dictionaries to add: "))
dict_list = []
for i in range(num_dicts):
    num_keys = int(input("Enter the number of keys to add for dictionary {}: ".format(i+1)))
    my_dict = {}
    for j in range(num_keys):
        key = input("Enter key {} for dictionary {}: ".format(j+1, i+1))
        value = input("Enter value for {}: ".format(key))
        my_dict[key] = value
    dict_list.append(my_dict)

print("The resulting list of dictionaries is:", dict_list)

dict_lst_asc = sorted(dict_list,key=lambda x: x[list(x.keys())[0]])
print("Ascending Order: ", dict_lst_asc)
dict_lst_desc = sorted(dict_list, key=lambda x: x[list(x.keys())[0]], reverse=True)
print("Descending Order: ", dict_lst_desc)
