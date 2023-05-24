def sep_list(jee,neet):
    only_neet = []
    only_jee = []
    both_exams = []
    atleast_one = []
    for i in jee:
        if i in neet:
            both_exams.append(i)
    print("People who have passed both the exams: ", both_exams)
    for i in jee:
        if i not in neet:
            only_jee.append(i)
    print("People who have passed only JEE: ", only_jee)
    for i in neet:
        if i not in jee:
            only_neet.append(i)
    print("People who have passed only NEET: ", only_neet)
    atleast_one = list(set(jee) | set(neet))
    print("People who have passed atleast one exam: ", atleast_one)
    


jeen = int(input("Enter the size of the list of people who have passed JEE: "))
jee = []
for i in range(jeen):
    name = input("Enter Name of Person " + str(i+1) + " : ")
    jee.append(name)

neetn = int(input("Enter the size of the list of people who have passed NEET: "))
neet = []
for i in range(neetn):
    name = input("Enter Name of Person " + str(i+1) + " : ")
    neet.append(name)

sep_list(jee,neet)
