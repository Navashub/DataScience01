"""
Booleans and Comparison Operators
Objective: Understand boolean values and comparison operators.
Task: Write a script that compares your age to 18 and prints whether you are older, younger, or exactly 18 years old.
"""

#Variable to ask user for the input of their age
my_age = int(input("Enter your age: "))
age = 18
if my_age == age:
    print("Exactly 18 years old.")
elif my_age < age:
    print("You are younger")
else:
    print("You are older")
