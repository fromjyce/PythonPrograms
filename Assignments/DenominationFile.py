import pickle

def get_denominations(amount, denominations):  
    count = [0] * len(denominations)  
    i = len(denominations) - 1  
    while (amount > 0 and i >= 0):  
        if (denominations[i] <= amount):  
            count[i] = amount // denominations[i]  
            amount = amount % denominations[i]  
        i -= 1  
    return count


def main():
    denom_dict = {} 
    amount = int(input("Enter the amount: "))
    denominations = [1, 5, 10, 50, 100, 500]  
    count = get_denominations(amount, denominations)  
    for i in range(len(denominations)):  
        if (count[i] > 0):  
            denom_dict[denominations[i]]=count[i]

    file = open("Denom_Dict.txt","a")
    file.write(str(denom_dict ))
    file.close()

  
if __name__ == '__main__':  
    main() 