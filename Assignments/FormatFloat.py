'''
Write a function to format the output of a float number which controls the number of digits 
and alignment. The function should be named as format_output() and takes two arguments, a 
float number x and a string which contains specifications for digits to print and alignment. 
'''

def format_output(num,form):
    formatted = format(num,form)
    print("The formatted output of floating number: ", formatted)

num = input("Enter a floating number: ")
choice = int(input("The Formatting types of Floating Number is given below: \n1. Specified Width: width.decimalnumberf \n2. Specified Precision: .decimalnumberf \n3. With Parentheses: (.decimalnumberf \n4. With Commas: ,.decimalnumberf \n5. Left Justification: <width.decimalnumberf \n6. Right Justification: >width.decimalnumberf \nEnter your Choice: "))
if choice == 1:
    floating_format = input("Enter format: [width.decimalnumberf]: ")
    format_output(float(num),floating_format)
elif choice == 2:
    floating_format = input("Enter format: [.decimalnumberf]: ")
    format_output(float(num),floating_format)
elif choice == 3:
    floating_format = input("Enter format: [(.decimalnumberf]: ")
    format_output(float(num),floating_format)
elif choice == 4:
    floating_format = input("Enter format: [,.decimalnumberf]: ")
    format_output(float(num),floating_format)
elif choice == 5:
    floating_format = input("Enter format: [<width.decimalnumberf]: " )
    format_output(float(num),floating_format)
elif choice == 6:
    floating_format = input("Enter format: [>width.decimalnumberf]: ")
    format_output(float(num),floating_format)
else:
    print("ENTER A VALID CHOICE!!")

