# Challenge 1:
# Naivas Supermarket sells two products: bread and milk.
# A loaf of bread weighs 400 grams. Each packet of milk is 0.5 litre.
# Write a program that reads the number of bread
# and the number of packets of milk in an order from the user.
# Then your program should compute and display the total quantity of the order.
# You should store the order in the dictionary and
# prompt the user for another input.
#

# def yourOrder():
#     order_dict = dict()
#     loaf_weight = 400
#     packet_weight = 0.5
#     while True:
#         order = input('What is your order? is it [bread or milk], and if you wish to exit, you can exit  ')
#         if order == 'bread':
#             breads = int(input('Enter the amount of breads: '))
#             quantity_of_breads = loaf_weight * breads
#             order_dict.update({"bread": (quantity_of_breads)})
#             print(order_dict)

#         elif order == 'milk':
#             packets = int(input("Enter the number of packets of milk: "))
#             quantity_of_milk = packet_weight * packets
#             order_dict.update({"milk": (quantity_of_milk)})
#             print(order_dict)


#         elif order == 'exit':
#             print(order_dict)
#             break

#         else:
#             print("invalid")
# yourOrder()


def yourOrders():
    while True:
        # Prompt the user for the number of bread and milk packets
        try:
            num_bread = int(input("Enter the number of loaves of bread (or type '0' to exit): "))
            if num_bread == 0:
                break
            num_milk = int(input("Enter the number of packets of milk: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

       
        weight_bread_per_loaf = 400  
        volume_milk_per_packet = 0.5  

        # Calculate the total weight and volume
        total_bread_weight = num_bread * weight_bread_per_loaf
        total_milk_volume = num_milk * volume_milk_per_packet

       
        order = {
            "number_of_bread": num_bread,
            "number_of_milk": num_milk,
            "total_bread_weight_grams": total_bread_weight,
            "total_milk_volume_liters": total_milk_volume
        }

       
        print(f"\nOrder Summary:")
        print(f"Number of loaves of bread: {order['number_of_bread']}")
        print(f"Total weight of bread: {order['total_bread_weight_grams']} grams")
        print(f"Number of packets of milk: {order['number_of_milk']}")
        print(f"Total volume of milk: {order['total_milk_volume_liters']} liters\n")


yourOrders()



