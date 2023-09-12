def change_to_hexadecimal(num):
    check_lst = ["1","A","0"]
    hex_dig = hex(num).replace("0x", "").upper()
    if len(hex_dig) <= 16 and all(hex_dig[j] in check_lst for j in range(len(hex_dig))):
        return True, hex_dig
    else:
        return False, hex_dig

def add_numbers(n):
    i = 0
    final_list = []
    for _ in range(n):
        cond , val = change_to_hexadecimal(i)
        if (cond == True):
            final_list.append(val)
        i+=1
    return len(final_list)

n = int(input("Enter the limit: "))
print(add_numbers(n))





