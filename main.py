import colorama
from colorama import Fore, Style


# Main function to start the game
def main():
    colorama.init()

    # Print the game's intro and narrative
    print(Fore.GREEN + "Welcome to Project Black Hat!" + Style.RESET_ALL)
    print(
        "\nYou are a skilled freelance hacker known only as 'Cipher'. You've been contracted by a mysterious client on the Dark Web to hack into the network of a powerful and secretive corporation known as 'Enigma Corp'. ")
    print(
        "\nYour mission: to steal sensitive information and expose their secrets."),
    print(
        "\nBut as you breach their defenses and delve deeper into their digital fortress, you stumble upon a dark and shocking secret that shakes you to your core.")
    print(
        "\nYou realize that this mission is not just about money or revenge, it's about justice.")
    print(
        "\nTorn between your loyalty to your client and your moral compass, you must make a choice. Do you continue the mission as planned, or do you risk everything to uncover the truth and bring Enigma Corp to justice?")
    print(
        "\nThe choice is yours. But remember, in the world of hacking, nothing is as it seems, and trust is a rare commodity.")
    print("\nLet's get started!")

    # Main menu loop
    while True:
        print("\nMain Menu:")
        print("Start")
        print("Exit")

        choice = input("Enter your choice: ")

        # Start the game
        if choice.lower() == "start":
            start_game()
        # Exit the game
        elif choice.lower() == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


# Function to start the game
def start_game():
    print("\nStarting game...")

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
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid command, please try again.")


# Function to connect to the network
def connect():
    print(Fore.YELLOW + "Connecting to Enigma Corps network..." + Style.RESET_ALL)

    # TODO: Implement hacking gameplay


# Function to access the mail system
def mail():
    print(Fore.BLUE + "Mail System:" + Style.RESET_ALL)

    # TODO: Implement mail system


# Function to display help message
def help_user():
    print(Fore.MAGENTA + "Help:" + Style.RESET_ALL)
    print("Use the 'connect' command to hack into Enigma Corps network.")
    print("Use the 'mail' command to view and respond to emails from your client and other characters.")
    print("Use the 'help' command if you need assistance at any time.")
    print("Use the 'exit' command to return to the Main Menu.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
