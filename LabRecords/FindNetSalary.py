#Finding the NET Salary
bs = int(input("Enter the basic salary: "))
d = int(input("Enter the dearance allowance (in percentage): "))
ds = (d/100)*bs
hra = int(input("Enter the House Rent Allowance: "))
ta = int(input("Enter the total allowance: "))
ch = input("Is there any tax cut? (Yes/No): ")
if ch == 'Yes' or ch == 'YES' or ch == 'yes':
  p = int(input("Enter the provident fund (in percentage): "))
  pf = (p/100)*bs
else:
  pf = 0
ns = (bs+ds+hra+ta)-pf
print ("Net Salary is Rs. " + str(ns))
