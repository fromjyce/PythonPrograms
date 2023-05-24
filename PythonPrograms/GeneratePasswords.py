import random
words = ["apple","cloak","hold", "freedom", "men", "dependence", "neighbour", "actaully","minister","every","beneath","drive","march","tree","boat","junior","mentioned","information","governor","stands","word","note","students","ordered","meaning","ceremony","hence","lower","stair","egg","property","sprite","here","rights"]
pw = []
num = int(input("Enter the number of passphrases do you want in password: "))
if num>len(words):
    print("ERROR!!!")
else:
    for i in range(num):
        word = random.choice(words)
        pw.append(word)

    passphrase = " ".join(pw)
    print("Your Passphrase is ", passphrase)

