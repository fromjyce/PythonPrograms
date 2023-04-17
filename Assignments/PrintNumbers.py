#Program that prints 0 to 6 except for 3 and 6
num = [0,1,2,3,4,5,6]
for i in num:
	if i==3 or i==6:
		num.remove(i)
		continue
print(num)


