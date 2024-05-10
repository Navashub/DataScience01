"""
Number Guessing Game (Python Numbers, Python If...Else)

Topics tested:
Python Numbers: Generating random numbers with random.randint() and converting user input to integers.
Python If...Else: Implementing conditional statements to provide feedback on the user's guesses.

Write a program that generates a random number between 1 and 100 and asks the user to guess it. 
Provide hints such as "too high" or "too low" after each guess.
Keep track of the number of guesses the user makes and congratulate them when they guess correctly.
"""

import random

a = random.randint(0, 100)

attempts = 0
your_guess = 0



while a != your_guess:
    your_guess = int(input("Guess a random number between 0 and 100: "))
    
    attempts += 1

    if (your_guess < a ):
        print("Too low")
    elif (your_guess > a):
        print("Too high")
    else:
        print(f"Congratulations you got it right after {attempts} attempts")








