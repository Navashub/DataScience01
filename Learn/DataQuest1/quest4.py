"""
Numbers and Operations
Objective: Practice working with numbers and arithmetic operations in Python.
Task: Write a script that calculates the area of a rectangle given its length and width.
"""

#ask user for the input of length and width and store in varables
rect_length = float(input("Length: "))
rect_width = float(input("Width: "))

#calculate the area using the formula
rectangle_area = rect_length * rect_width

print(f"Given a rectangle of Length {rect_length} and Width of {rect_width} its Area is: {rectangle_area}")
