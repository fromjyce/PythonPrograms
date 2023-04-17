# Using the slicing operation on string representing URLs of websites, check the following and print appropriate messages
url = input("Enter the URL: ")
if url.startswith("http:") == True or url.startswith("https:") == True or url.startswith("ftp:") == True:
    print("The Input URL starts with the appropriate substring")
else:
    print("The Input URL doesn't start with the appropriate substring")
if url.endswith(".com") == True or url.endswith(".org") == True or url.endswith(".in") == True:
    print("The Input URL ends with the appropriate substring")
else:
    print("The Input URL doesn't end with the appropriate substring")
