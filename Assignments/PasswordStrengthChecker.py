pw = input("Enter a password: ")
l = u = d = s = c = 0
if len(pw)>=8 and len(pw)<=16:
    for i in pw:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            d+=1
        if i=='@' or i== '!' or i=='#' or i=='$' or i=='%' or i == '&' or i == '*':
            s+=1
if l>=1:
    c+=1
if u>=1:
    c+=1
if d>=1:
    c+=1
if s>=1:
    c+=1
if c==4:
    print("PASSWORD STRENGTH IS STRONG")
if c==3 or c==2:
    print("PASSWORD STRENGTH IS MEDIUM")
if c==1:
    print("PASSWORD STRENGTH IS POOR")
if c==0:
    print("INVALID PASSWORD")
