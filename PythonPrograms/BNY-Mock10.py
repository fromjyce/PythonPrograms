messages = input().split(" ")
nums = [int(c) for c in messages if c.isdigit()]
not_nums = [c for c in nums if "9" not in str(c)]


mess = max(not_nums) if len(nums) != 0 else -1
print(mess)