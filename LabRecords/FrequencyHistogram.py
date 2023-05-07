import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

title = input("What is the title of your histogram: ")
num_tuples = int(input("How many pairs do you want to enter: "))
data = []
for i in range(num_tuples):
    pair = input(f"Enter pair {i+1} (in the format 'value, number'): ")
    pair = tuple(pair.split(","))
    data.append(pair)
print("Inputted data:", data)
ind = []
fre = []
for item in data:
   ind.append(item[0])
   fre.append(item[1])

plt.title(title)
plt.bar(ind, fre)

plt.show()