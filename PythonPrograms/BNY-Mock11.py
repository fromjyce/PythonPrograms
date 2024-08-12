nums = [100.00, 489.12, 12454.12, 1234.10, 823.05, 109.20, 5.27, 1542.25, 839.18, 83.99, 1295.01, 1.75]

cnt = 1

nums_t = []

'''
while True:
    val = float(input())
    nums.append(val)
    if cnt == 12:
        break
    cnt += 1
'''

print(nums)

avg_nums = sum(nums) / len(nums)

print(avg_nums)

mess = "$"+str(round(avg_nums,2))

print(mess)