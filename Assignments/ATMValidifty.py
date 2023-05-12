'''
Write a Python Script to build ATM Machine functionality 
Acceptance Criteria:
a) create a python function which askes ATM Pin as Input and if the Pin is Valid means it 
should display Withdraw and Check Account balance option. (Use string functions to check 
if a pin has only 4 numeric characters).
b) create a python function which allows user to select the option
c) create a separate python function which implements check account balance and withdraw 
functionality.
d) After the successful withdrawal account balance should reduce
e) If an user enters invalid withdrawal, you should notify the user with error message
'''

balance = 1000000
pin =input("Enter the ATM Pin: ")
if len(pin) == 4 and all(x.isnumeric() for x in pin):
    while(1):
        choice = int(input("1. Withdrawal \n2. Check Balance \nEnter your choice: "))
        if choice == 1: 
            amount = int(input("Amount that should be withdrawn: "))
            balance = balance - amount
            print(str(amount) + " withdrawn successfully")
        elif choice == 2:
            print("Balance: " + str(balance))
        else:
            print("Enter VALID Choice!!!")
else:
    print("INVALID PIN")