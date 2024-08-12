from collections import Counter

low = int(input())
high = int(input())

count = 0

for i in range(low, high+1):
    if (len(Counter(str(i))) == len(str(i))):
        count += 1


print(count)