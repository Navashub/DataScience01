"""
Challenge 1: Mad Libs Generator (Python Strings, Python Input/Output)

Topics tested:
Python Strings: String formatting with f-strings.
Python Input/Output: Taking user input and printing output.

Create a Mad Libs generator program that asks the user for various types of words (noun, verb, adjective, etc.) and then generates a story using those words. 
Use string formatting to insert the user's input into the story template.
"""

#Taking users input 
name = input("Name: ")
age = int(input("Age: "))
institution = input("Institution: ")
subject = input("Course: ")

print(f"I am {name}, {age} years old taking {subject} in {institution} institution.")



