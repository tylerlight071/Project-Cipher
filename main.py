import colorama
from colorama import Fore, Style
import time
from IPython.display import clear_output

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Main function to start the game
def main():
    colorama.init()
    print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "  ____  _            _      _   _       _   " + Style.RESET_ALL)
    print_slow(Fore.GREEN + " | __ )| | __ _  ___| | __ | | | | __ _| |_ " + Style.RESET_ALL)
    print_slow(Fore.GREEN + " |  _ \\| |/ _` |/ __| |/ / | |_| |/ _` | __|" + Style.RESET_ALL)
    print_slow(Fore.GREEN + " | |_) | | (_| | (__|   <  |  _  | (_| | |_ " + Style.RESET_ALL)
    print_slow(Fore.GREEN + " |____/|_|\\__,_|\\___|_|\\_\\ |_| |_|\\__,_|\\__|" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "                                            " + Style.RESET_ALL)
    print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)

    # Print the game's intro and narrative
    print_slow(
        "\nYou are a skilled freelance hacker known only as 'Cipher'. You've been contracted by a mysterious client on the Dark Web to hack into the network of a powerful and secretive corporation known as 'Enigma Corp'. ")
    print_slow(
        "\nYour mission: to steal sensitive information and expose their secrets."),
    print_slow(
        "\nBut as you breach their defenses and delve deeper into their digital fortress, you stumble upon a dark and shocking secret that shakes you to your core.")
    print_slow(
        "\nYou realize that this mission is not just about money or revenge, it's about justice.")
    print_slow(
        "\nTorn between your loyalty to your client and your moral compass, you must make a choice. Do you continue the mission as planned, or do you risk everything to uncover the truth and bring Enigma Corp to justice?")
    print_slow(
        "\nThe choice is yours. But remember, in the world of hacking, nothing is as it seems, and trust is a rare commodity.")
    print_slow("\nLet's get started!")

    # Pause for 2 seconds before clearing the console
    time.sleep(2)

    # Clear the console
    clear_output(wait=True)

    # Main menu loop
    while True:
        print_slow("\nMain Menu:")
        print_slow("Start")
        print_slow("Exit")

        choice = input("Enter your choice: ")

        # Start the game
        if choice.lower() == "start":
            start_game()
        # Exit the game
        elif choice.lower() == "exit":
            print_slow("Exiting...")
            break
        else:
            print_slow("Invalid choice, please try again.")


# Function to start the game
def start_game():
    print_slow("\nStarting game...")

    # Game command loop
    while True:
        command = input("> ")

        # Connect to the network
        if command == "connect":
            connect()
        # Access the mail system
        elif command == "mail":
            mail()
        # Display help message
        elif command == "help":
            help_user()
        # Return to the main menu
        elif command == "exit":
            print_slow("Returning to Main Menu...")
            break
        else:
            print_slow("Invalid command, please try again.")


# Function to connect to the network
def connect():
    print_slow(Fore.YELLOW + "Connecting to Enigma Corps network..." + Style.RESET_ALL)

    # TODO: Implement hacking gameplay


# Function to access the mail system
def mail():
    print_slow(Fore.BLUE + "Mail System:" + Style.RESET_ALL)

    # TODO: Implement mail system


# Function to display help message
def help_user():
    print_slow(Fore.MAGENTA + "Help:" + Style.RESET_ALL)
    print_slow("Use the 'connect' command to hack into Enigma Corps network.")
    print_slow("Use the 'mail' command to view and respond to emails from your client and other characters.")
    print_slow("Use the 'help' command if you need assistance at any time.")
    print_slow("Use the 'exit' command to return to the Main Menu.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
