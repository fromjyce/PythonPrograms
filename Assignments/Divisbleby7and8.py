'''
Generate a list within a specific range of values. Find the numbers from this list which 
are divisible by 7 and 8 and print them in a separate list.
'''

lower = int(input("Enter the lower limit: "))
higher = int(input("Enter the higher limit: "))
lst = []
print_lst = []
for i in range(lower,higher+1):
    lst.append(i)

for i in lst:
    if i % 7 == 0 and i % 8 == 0:
        print_lst.append(i)

if print_lst:
    print("NUMBERS THAT ARE DIVISIBLE BY SEVEN AND EIGHT: ", print_lst)
else:
    print("NO NUMBERS DIVISBLE BY SEVEN AND EIGHT WERE FOUND IN THE INPUT RANGE")

        