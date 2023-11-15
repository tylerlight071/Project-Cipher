import random
from colorama import Fore, Style

def code_shatter_minigame():
    # Generate a random 5-digit number
    target = [str(random.randint(1, 9)) for _ in range(5)]
    
    print("Welcome to CodeShatter!")
    print("Guess the 5-digit number.")
    print("Green: Correct digit in correct position.")
    print("Orange: Correct digit in incorrect position.")
    print("Red: Incorrect digit.")
    
    attempts = 0
    while attempts < 10:
        # Get the user's guess
        guess = input("Enter your guess: ")
        
        if len(guess) != 5 or not guess.isdigit():
            print("Invalid input. Please enter a 5-digit number.")
            continue
        
        attempts += 1
        
        # Check the guess against the target
        feedback = []
        for i in range(5):
            if guess[i] == target[i]:
                feedback.append(Fore.GREEN + guess[i] + Style.RESET_ALL)
            elif guess[i] in target:
                feedback.append(Fore.YELLOW + guess[i] + Style.RESET_ALL)
            else:
                feedback.append(Fore.RED + guess[i] + Style.RESET_ALL)
        
        print("Feedback: " + " ".join(feedback))
        
        # Check if the guess is correct
        if guess == "".join(target):
            print("Congratulations! You guessed the correct number!")
            break
    else:
        print("Sorry, you've run out of attempts. The correct number was " + "".join(target) + ".")