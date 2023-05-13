lower = int(input("Enter the lower limit: "))
higher = int(input("Enter the higher limit: "))

prime_lst = []

for num in range(lower, higher + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_lst.append(num)

print("Prime numbers between", lower, "and", higher, "are:", prime_lst)
