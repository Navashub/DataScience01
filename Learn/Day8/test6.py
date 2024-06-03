# Challenge 3
# Upon creating the Naivas supermarket dictionary program earlier on,
# We will now extend the functionality of your program to be able to also update
# the quantity of either the bread or packet of milk.
# Write another program the will prompt the user to indicate whether they want
# to update the quantity of the product or compute the total quantity of the total order.
# Using if statements, your program should execute either to the code you had earlier
# on written or to the new code for updating that you will now write
#


def yourOrders():
    order = {
        "number_of_bread": 0,
        "number_of_milk": 0,
        "total_bread_weight_grams": 0,
        "total_milk_volume_liters": 0
    }
    
    def total_quantity():
        # Prompt the user for the number of bread and milk packets
        try:
            breads = int(input("Enter the number of loaves of bread: "))
            milk = int(input("Enter the number of packets of milk: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        
        weight_bread_per_loaf = 400  # grams
        volume_milk_per_packet = 0.5  # l

        # Calculate the total weight and volume
        total_bread_weight = breads * weight_bread_per_loaf
        total_milk_volume = milk * volume_milk_per_packet

        # Update the order in the dictionary
        order["number_of_bread"] = breads
        order["number_of_milk"] = milk
        order["total_bread_weight_grams"] = total_bread_weight
        order["total_milk_volume_liters"] = total_milk_volume

        # SDisplay the total quantities
        print(f"Number of loaves of bread: {order['number_of_bread']}")
        print(f"Total weight of bread: {order['total_bread_weight_grams']} grams")
        print(f"Number of packets of milk: {order['number_of_milk']}")
        print(f"Total volume of milk: {order['total_milk_volume_liters']} liters\n")
    
    def update_quantity():
        product = input("Which product do you want to update (bread/milk)? ").strip().lower()
        if product not in ["bread", "milk"]:
            print("Invalid product. Please enter 'bread' or 'milk'.")
            return
        
        try:
            new_quantity = int(input(f"Enter the new quantity for {product}: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if product == "bread":
            order["number_of_bread"] = new_quantity
            order["total_bread_weight_grams"] = new_quantity * 400  
        elif product == "milk":
            order["number_of_milk"] = new_quantity
            order["total_milk_volume_liters"] = new_quantity * 0.5  
        
        print(f"Number of loaves of bread: {order['number_of_bread']}")
        print(f"Total weight of bread: {order['total_bread_weight_grams']} grams")
        print(f"Number of packets of milk: {order['number_of_milk']}")
        print(f"Total volume of milk: {order['total_milk_volume_liters']} liters\n")
    
    while True:
        action = input("Do you want to compute the total quantity or update a product quantity? (compute/update/exit): ").strip().lower()
        if action == "compute":
            total_quantity()
        elif action == "update":
            update_quantity()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please enter 'compute', 'update', or 'exit'.")

yourOrders()
