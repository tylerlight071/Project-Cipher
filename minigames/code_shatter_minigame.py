import random
from colorama import Fore, Style
from components.print_slow.print_slow import print_slow

def code_shatter_minigame():
    print("Debug: Entering CodeShatter MiniGame")
    # Generate a random 5-digit number
    target = [str(random.randint(1, 9)) for _ in range(5)]

    print_slow("Welcome to CodeShatter!")
    print_slow("")
    print_slow("Guess the 5-digit number.")
    print_slow("")
    print_slow("The sequence can contain multiple same numbers")
    print_slow("")
    print_slow(Fore.GREEN + "Green: Correct digit in correct position." + Style.RESET_ALL)
    print_slow("")
    print_slow(Fore.YELLOW + "Orange: Correct digit in incorrect position." + Style.RESET_ALL)
    print_slow("")
    print_slow(Fore.RED + "Red: Incorrect digit." + Style.RESET_ALL)
    print_slow("")

    attempts = 0
    while attempts < 7:
        # Get the user's guess
        guess = input("Enter your guess: ")

        if len(guess) != 5 or not guess.isdigit():
            print_slow("Invalid input. Please enter a 5-digit number.")
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
            print_slow(Fore.GREEN + "Access granted." + Style.RESET_ALL)
            break
    else:
        print_slow(Fore.RED + "Access denied. Too many attempts." + Style.RESET_ALL)

