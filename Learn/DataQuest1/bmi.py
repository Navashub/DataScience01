"""
Challenge 2 : BMI Calculator:

Tests your skill on:
User input handling
Basic arithmetic operations
Conditional statements
Output formatting

Challenge: Write a Python program that calculates the Body Mass Index (BMI) based on user input of weight (in kilograms) and height (in meters).

Requirements:
Prompt the user to input their weight in kilograms.
Prompt the user to input their height in meters.
Calculate the BMI using the formula: BMI = weight / (height * height).
Print the calculated BMI and interpret it according to BMI categories (e.g., underweight, normal weight, overweight, obese).
"""

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
squared_height = height * height
BMI = weight/squared_height

if BMI <18.5:
    print("Underweight")
elif BMI < 24.9:
    print("Normal")
elif BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")