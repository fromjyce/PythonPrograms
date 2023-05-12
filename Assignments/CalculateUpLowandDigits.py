# Write a python function that takes a string and calculates the number of upper, lower and digits present in the string and print the same.
word = input("Enter a string/word: ")
u = l = d = 0

print("Digits available in the String/Word: ")
for i in word:
    if i.isdigit() == True:
        d=d+1
        print(i)
print("Count: " + str(d))

print("Lower Alphabets available in String/Word: ")
for i in word:
    if i.islower() == True:
        l = l+1
        print(i)
print("Count: " + str(l))

print("Lower Alphabets available in String/Word: ")
for i in word:
    if i.isupper() == True:
        u = u+1
        print(i)
print("Count: " + str(u))
