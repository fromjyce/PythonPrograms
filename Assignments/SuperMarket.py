supermarket = {
    "milk": {"quantity": 20, "price": 25.00},
    "biscuits": {"quantity": 32, "price": 20.00},
    "butter": {"quantity": 20, "price": 70.50},
    "cheese": {"quantity": 15, "price": 82.50},
    "bread": {"quantity": 15, "price": 45.00},
    "cookies": {"quantity": 20, "price": 52.80},
    "yogurt": {"quantity": 18, "price": 41.30},
    "apples": {"quantity": 35, "price": 120.40},
    "oranges": {"quantity": 40, "price": 60.50},
    "bananas": {"quantity": 23, "price": 50.00}
}

customers = ["Frank", "Mary", "Paul"]

shopping = {
    "Frank": [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
    "Mary": [('apples', 2), ('cheese', 4), ('bread', 2), ('pears', 3), ('bananas', 4), ('oranges', 1), ('cherries', 4)],
    "Paul": [('biscuits', 2), ('apples', 3), ('yogurt', 2), ('pears', 1), ('butter', 3), ('cheese', 1), ('milk', 1),
             ('cookies', 4)]
}

def create_receipt(customer_name, items):
    total_sum = 0
    receipt = []

    for item_name, quantity in items:
        if item_name in supermarket:
            item_data = supermarket[item_name]
            item_quantity = item_data["quantity"]
            item_price = item_data["price"]

            if item_quantity >= quantity:
                item_sum = item_price * quantity
                receipt.append(f"{quantity}, {item_name}, {item_price}, {item_sum}")
                total_sum += item_sum
                supermarket[item_name]["quantity"] -= quantity
            else:
                receipt.append(f"Insufficient quantity for {item_name}")
        else:
            receipt.append(f"Invalid item: {item_name}")

    receipt.append(f"Total sum: {total_sum}")
    return receipt

for customer in customers:
    customer_shopping = shopping.get(customer, [])
    receipt = create_receipt(customer, customer_shopping)
    print(f"Receipt for {customer}:")
    for item in receipt:
        print(item)
    print()
