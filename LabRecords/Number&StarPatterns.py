#Generation of Number Pattern and Star Pattern
choice1 = int(input("Do you want \n1. Number Pattern (0 to 9) \n2. Star Pattern \nEnter your choice: "))
choice2 = int(input("Do you want \n1. Square Pattern \n2. Left Lower Triangular Pattern \n3. Right Lower Triangular Pattern \n4. Left Upper Triangular Pattern \n5. Straight Pyramid \n6. Inverted Pyramid \nEnter your choice: "))
if choice1==1:
		if choice2==1:
			row = int(input("Enter the number of rows: "))
			for i in range (row):
				for j in range (0,10):
					print(j+1, end = ' ')
				print()
			exit()
		elif choice2==2:
			row = int(input("Enter the number of rows: "))
			for i in range (row+1):
				for j in range(1,i+1):
					print(j, end = ' ')
				print ()
			exit()
		elif choice2==3:
			row = int(input("Enter the number of rows: "))
			for i in range(row):
				for j in range(1, row-i):
					print (" ", end = " ")
				for k in range(1, i+2):
					print (k, end = ' ')
				print()
			exit()
		elif choice2==4:
			row = int(input("Enter the number of rows: "))
			for i in range(0, row+1):
				for j in range(row-i, 0, -1):
					print(j, end=' ')
				print()
			exit()
		elif choice2==5:
			row = int(input("Enter the number of rows: "))
			for i in range (row):
				for j in range(row-i-1):
					print(' ', end = ' ')
				for k in range(2*i+1):
					print(k+1, end=' ')
				print()
			exit()
		elif choice2==6:
			row=int(input("Enter the number of rows: "))
			for i in range(row):
				for j in range(i):
					print(' ', end=' ')
				for j in range(2*(row-i)-1):
					print(j+1, end = ' ')
				print()
			exit()
		else:
			print("INVALID NUMBER")
			exit()
if choice1==2:
		if choice2==1:
			row=int(input("Enter the number of rows: "))
			for i in range(row):
				for j in range(row):
					print('*', end=' ')
				print()
			exit()
		elif choice2==2:
			row=int(input("Enter the number of rows: "))
			for i in range(row+1):
				for j in range(1,i+1):
					print('*', end=' ')
				print()
			exit()
		elif choice2==3:
			row=int(input("Enter the number of rows: "))
			for i in range(row):
				for j in range(1, row-i):
					print(' ', end=' ')
				for k in range(1, i+2):
					print('*', end = ' ')
				print()
			exit()
		elif choice2==4:
			row = int(input("Enter the number of rows: "))
			for i in range(0, row+1):
				for j in range(row-i, 0, -1):
					print('*', end =' ')
				print()
			exit()
		elif choice2==5:
			row = int(input("Enter the number of rows: "))
			for i in range(row):
				for j in range(row-i-1):
					print(' ', end = " ")
				for k in range(2*i+1):
					print('*', end = " ")
				print()
			exit()
		elif choice2==6:
			row = int(input("Enter the number of rows: "))
			for i in range(row):
				for j in range(i):
					print(" ", end=" ")
				for k in range(2*(row-i)-1):
					print("*", end = " ")
				print()
			exit()
		else:
			print("INVALID NUMBER")
			exit()
else:
	print("INVALID NUMBER")
	exit()
	
