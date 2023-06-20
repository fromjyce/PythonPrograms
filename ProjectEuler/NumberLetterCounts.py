#If all the numbers from Lower limit to upper limit inclusive were written out in words, how many letters would be used?
from num2words import num2words

def generate_letters(lower,upper):
    num_list = []
    for i in range(lower, upper + 1):
        num_word = num2words(i)
        num_list.append(num_word.replace(" and ", " "))  
    return num_list

def count_letters(num_list):
    sum = 0
    for i in num_list:
        for j in i:
            if j.isalpha():
                sum+=1
    return sum

    


lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))
print(count_letters(generate_letters(lower,upper)))
