#Program that calculates the total grades
num = int(input("Enter the number of subjects: "))
sum = 0
grade = {}
for i in range(0,num):
		name = input("Name of the Subject " + str(i+1) + ": ")
		mark = int(input("Marks obtained in " + name.title() + " (out of 100): "))
		grade.update({name:str(mark)})
		sum=sum+mark
print("\nMarks obtained in each Subject: ")
for name, mark in grade.items():
		print(name.title() + " - " + str(mark) + "/100")
total = 100*num
perc = (sum*100)//total
if perc>=91 or perc<100:
		alp = "A1"
elif perc>=81 or perc<90:
		alp = "A2"
elif perc>=71 or perc<80:
		alp = "B1"
elif perc>=61 or perc<70:
		alp = "B2"
elif perc>=51 or perc<60:
		alp = "C1"
elif perc>=41 or perc<50:
		alp = "C2"
elif perc>=33 or perc<40:
		alp = "D"
else:
		alp = "Reappear"
print("\nTotal Marks obtained: " + str(sum) + "/" + str(total) + "\nPercentage obtained: " + str(perc) + "%" + "\nGrade: " + alp)
