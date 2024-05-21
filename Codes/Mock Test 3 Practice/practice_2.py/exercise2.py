def shopping(alist, stock):
    # return (spent (total money spent), missing (new shopping list))
    # alist is the shopping list alist[item] = quantity_needed, stock[item] = (quantity_stocked, price)
    spent = 0
    missing = {}

    for item in alist:
        quantity_needed = alist[item]
        # product_price = stock[item][1]
        # quantity_stocked = stock[item][0]

        #item not on stock
        if item not in stock:
            missing[item] = quantity_needed
        
        #not enough stock
        elif stock[item][0] < quantity_needed:
            spent += stock[item][0] * stock[item][1]
            missing[item] = quantity_needed - stock[item][0]

        #default -> item in stock with the quantity needed
        else:
            spent += quantity_needed*stock[item][1]

    return (spent, missing)


# print(shopping({'banana': 10, 'apples': 20, 'oranges': 30}, {'banana': (30, 3), 'apples': (10, 2)}))