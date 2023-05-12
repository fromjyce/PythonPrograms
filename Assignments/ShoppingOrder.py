'''
For an online shopping application, a dictionary data structure is used to store the collection of products and their prices. Write a Python code to perform the following:
	    Display all the products with its price to the customer.
	    Read the order from the customer, if the ordered product is in the dictionary, then print the product id and price, if not present, ask the customer to reorder.
'''

shopping_items = {"Pencil":7, "Pen":8, "Sharpener":5, "Scale":10, "Eraser": 4, "PenPencil": 15, "Whitener":25, "Pelican":5, "Ink Eraser":20, "Stapler":90}
while(1):
    choice = int(input("1. Order an item \n2. Display the items \nEnter your choice: "))
    if choice == 1:
        item = input("Enter the element that you want to order: ")
        if item.title() in shopping_items.keys():
            quantity = int(input("Enter the quantity: "))
            if quantity>0:
                total_amt = quantity * shopping_items[item.title()]
                print("Total Amount: Rs. ", total_amt)
            else:
                print("Please, Atleast buy one item")
        else:
            print("Item Not Available, Reorder Again")
    elif choice == 2:
        print("Available Items: ")
        print(shopping_items)
    else:
        print("Enter Valid Choice")