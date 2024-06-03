# Welcome message
print("Welcome to Python Pizza Deliveries!")

# Prompt user for pizza size
size = input("What size pizza do you want? S, M, or L: ")

# Prompt user for pepperoni
add_pepperoni = input("Do you want pepperoni? Y or N: ")

# Prompt user for extra cheese
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Initialize the bill
bill = 0

# Calculate the base price based on pizza size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add the cost of pepperoni if requested
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add the cost of extra cheese if requested
if extra_cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your final bill is: ${bill}.")
