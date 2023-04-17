# Write a Python function that takes two strings and return a string where the first two characters of each string are swapped and separated by space. E.g.: 'abc', 'xyz' o/p: 'xyc abz'. Validate the input such that if the length of either of the strings is less than 3, print error message saying “Enter a valid string with length more than 3”.
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if len(str1)>=3 and len(str2)>=3:
    str3 = " ".join([str1.replace(str1[0:-1],str2[0:-1]),str2.replace(str2[0:-1],str1[0:-1])])
    print(str3)
else:
    print("Enter a valid string with length more than 3")   
