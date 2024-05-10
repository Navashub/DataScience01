
while True:
    #restart the game and generate number to guess
    number1 = random.randint(0,10)
    attempts  = 0
    
    guess = int(input("guess a random number between 0 and 10. "))
    attempts += 1
    
    #repeat this logic while the guess is not correct
    while guess!=number1:
        if guess > number1:
            print("try a smaller number. ")
        else:
            print("try a bigger number. ")
        guess = int(input("guess a random number between 0 and 10. "))
    
    #ask to continue once the previous game is completed
    playAgain = input(f"correct! the secret number was indeed {number1}, and you guessed it in {attempts} attempts. play again? (yes/no)")
    if playAgain == "no":
        break