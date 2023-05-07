num_tuples = int(input("How many tuples do you want to enter? "))
data = []
for i in range(num_tuples):
    pair = input(f"Enter pair {i+1} (in the format 'value, number'): ")
    pair = tuple(pair.split(","))
    data.append(pair)
print("Inputted data:", data)
