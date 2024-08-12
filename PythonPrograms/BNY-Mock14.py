cstr = input()

print(cstr)

res = []

for i in cstr:
    if i.isupper() and res:
        res.append(" ")
    res.append(i)
print(''.join(res).lower())