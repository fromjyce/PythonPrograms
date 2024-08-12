from itertools import permutations

def small_num(a,b):
    num_str = str(a)
    perm = permutations(num_str)
    perm_as = {int(''.join(p)) for p in perm}

    filtered_perm_as = [x for x in perm_as if x > b]
    return min(filtered_perm_as) if filtered_perm_as else -1

s_nums = input()
nums = [int(num) for num in s_nums.split(" ")]
a = nums[0]
b = nums[1]



result = small_num(a,b)
print(result,type(result))
