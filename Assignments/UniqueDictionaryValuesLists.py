dictionary = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, 
{"V":"S009"},{"VIII":"S007"}]
unq_list = []
for i in dictionary:
    for key in i:
        a=i[key]
        unq_list.append(a)

sorted_list = sorted(set(unq_list))
print(sorted_list)