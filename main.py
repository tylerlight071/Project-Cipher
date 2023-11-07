import os
import pickle
import colorama
from colorama import Fore, Style
import time
from IPython.display import clear_output
from systems.level_1.amy_system import AmySystem

# Set the PYGAME_HIDE_SUPPORT_PROMPT environment variable
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the bg music file and loop it
pygame.mixer.music.load('bg_music.mp3')
pygame.mixer.music.play(-1)

# sets the volume to 20% (change value to adjust)
pygame.mixer.music.set_volume(0.2)

# Define the global variables at the module level
inventory = []
balance = 300
emails = []
has_read_email = False
amy_system = AmySystem()


# Save the game state to a file
# Save the game state to a file
def save_game():
    global inventory, balance, emails, has_read_email  # Add has_read_email here
    with open('savegame.pkl', 'wb') as f:
        pickle.dump((inventory, balance, emails, has_read_email), f)  # Add has_read_email here


# Load the game state from a file
def load_game():
    global inventory, balance, emails, has_read_email  # Add has_read_email here
    if os.path.exists('savegame.pkl'):
        with open('savegame.pkl', 'rb') as f:
            inventory, balance, emails, has_read_email = pickle.load(f)  # Add has_read_email here
    else:
        # If the savegame file doesn't exist, set the default values
        inventory = []
        balance = 300
        emails = [
            {
                "sender": "Prophet",
                "subject": "Prove Your Loyalty",
                "body": (
                    "Cipher, welcome to the ranks of the resistance. You've been chosen to join our clandestine operation against Enigma Corp, "
                    "and your unique skills are crucial to our mission of exposing their "
                    "\nsecrets and bringing them to justice."
                    "\n\nTo demonstrate your allegiance, you must first acquire the 'EnigmaLink' application from the Hacker's Market. "
                    "EnigmaLink is no ordinary tool—it contains a back door, covertly planted by our operatives, which"
                    "\nwill grant you access to Enigma Corps servers."
                    "\n\nUpon obtaining EnigmaLink, initiate your infiltration by using the 'connect' command. "
                    "Once inside, navigate the labyrinth of their network, extracting any valuable intelligence that could tip the scales in "
                    "\nour favor."
                    "\n\nEvery piece of information you gather is vital to our cause, so be meticulous and thorough."
                    "Your success is paramount, Cipher. The fate of our operation rests on your shoulders."
                )
            },
        ]
        has_read_email = False


# Initialize the user's inventory and balance
load_game()


# Function to add an item to the inventory
def add_to_inventory(item):
    inventory.append(item)


# Function to check if an item is in the inventory
def has_item(item):
    return item in inventory


# Makes the text have a delay of (x) when printed to screen
def print_slow(text, delay=0.00):  # change to 0.01
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# Prints the games title
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
        "\nYou are a skilled freelance hacker known only as 'Cipher'. You've been contracted by a mysterious organisation known as The Resistance to hack "
        "\ninto the network of a powerful and secretive corporation known as 'Enigma Corp'. ")
    print_slow("\n\nYour mission: to steal sensitive information and expose their secrets."),
    print_slow(
        "\n\nBut as you breach their defenses and delve deeper into their digital fortress, you stumble upon a dark and shocking secret that shakes you to your core.")
    print_slow("\nYou realize that this mission is not just about money or revenge, it's about justice.")
    print_slow(
        "\nTorn between the payout and your moral compass, you must make a choice. Do you continue the mission as planned, or do you risk everything to uncover the truth and bring Enigma Corp to justice?")
    print_slow(
        "\nThe choice is yours. But remember, in the world of hacking, nothing is as it seems, and trust is a rare commodity.")
    print_slow("\nLet's get started!")

    # Pause for 2 seconds before clearing the console
    time.sleep(2)

    # Clear the console
    clear_output(wait=True)

    # Main menu loop
    while True:
        print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "|                 Main Menu                  |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Start]  Start the game                    |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Exit]   Exit the game                     |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)

        choice = input(Fore.GREEN + "\n> " + Style.RESET_ALL)

        # Start the game
        if choice.lower() == "start":
            start_game()
        # Exit the game
        elif choice.lower() == "exit":
            print_slow(Fore.GREEN + "\nExiting..." + Style.RESET_ALL)
            pygame.mixer.music.stop()
            break
        else:
            print_slow(Fore.RED + "\nInvalid choice, please try again." + Style.RESET_ALL)


# Function to get the user's balance
def get_balance():
    return balance


# Function to add money to the user's balance
def add_money(amount):
    global balance
    balance += amount


# Function to subtract money from the user's balance
def subtract_money(amount):
    global balance
    balance -= amount


# Function to print the user's balance
def print_balance():
    print(f"Your current balance is: £{get_balance()}")


def read_email(emails, subject):
    global has_read_email
    for email in emails:
        if email['subject'].lower() == subject.lower():
            # If the email is from Prophet, set has_read_email to True
            if email['sender'].lower() == 'prophet':
                has_read_email = True
            print_slow(
                Fore.LIGHTBLUE_EX + f"\nFrom: {email['sender']}\nSubject: {email['subject']}\n\n{email['body']}" + Style.RESET_ALL)
            return
    print_slow(Fore.RED + "\nNo email found with that subject, please try again." + Style.RESET_ALL)


# List of available upgrades
upgrades = [
    {"name": "EnigmaLink", "description": "Application required to connect to Enigma Corps network.", "price": 300},
    {"name": "Stealth Mode", "description": "Makes your hacks undetectable.", "price": 200},
    {"name": "Firewall Bypass", "description": "Allows you to bypass firewalls easily.", "price": 300}
]


# Function to display the shop
def shop():
    if not has_read_email:
        print_slow(Fore.RED + "\nI should check my emails first...")
        return
    print_slow(Fore.YELLOW + r'''      ____  _               _       
     / ___|| |__   __ _ ___| | _____ 
     \___ \| '_ \ / _` / __| |/ / __|
      ___) | | | | (_| \__ \   <\__ \
     |____/|_| |_|\__,_|___/_|\_\___/''' + Style.RESET_ALL)

    print_slow(Fore.YELLOW + "\nWelcome to the Hacker's Market!" + Style.RESET_ALL)
    print_slow(Fore.YELLOW + "Here you can buy upgrades to improve your hacking abilities.\n" + Style.RESET_ALL)

    while True:
        # Display the list of available upgrades
        for i, upgrade in enumerate(upgrades):
            print_slow(
                Fore.YELLOW + f"{i + 1}. {upgrade['name']} - {upgrade['description']} - £{upgrade['price']}" + Style.RESET_ALL)

        # Get the user's choice
        command = input(Fore.YELLOW + "\n> " + Style.RESET_ALL)

        # Buy the chosen upgrade
        if command.lower() == 'exit':
            break
        elif command.lower() == 'help':
            shop_help()
        elif command.lower().startswith('buy '):
            upgrade_name = command[4:]
            for upgrade in upgrades:
                if upgrade_name.lower() == upgrade['name'].lower():
                    if get_balance() >= upgrade['price']:
                        print_slow(
                            Fore.GREEN + f"You have successfully purchased {upgrade['name']} for ${upgrade['price']}!" + Style.RESET_ALL)
                        subtract_money(upgrade['price'])
                        print_balance()
                        add_to_inventory(upgrade['name'])
                    else:
                        print_slow(Fore.RED + "You don't have enough money to buy this upgrade." + Style.RESET_ALL)
                    break
            else:
                print_slow(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)
        else:
            print_slow(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)


# Function to start the game
def start_game():
    print_slow("\nStarting game...")
    time.sleep(1)
    print_slow("\nLoading assets...")
    time.sleep(1)
    # Print a hint message to the user
    print_slow(Fore.MAGENTA + "\nHint:  Type 'help' to get a list of available commands." + Style.RESET_ALL)

    # Game command loop
    while True:
        command = input(Fore.GREEN + "> " + Style.RESET_ALL)

        # Connect to the network
        if command.lower() == "connect":
            connect()
        # Access the mail system
        elif command.lower() == "mail":
            mail()
        # Display help message
        elif command.lower() == "help":
            help_user()
        # Check balance
        elif command.lower() == "balance":
            print_balance()
        elif command.lower() == "shop":
            shop()
        # Return to the main menu
        elif command.lower() == "exit":
            print_slow("Returning to Main Menu...")
            break
        else:
            print_slow("Invalid command, please try again.")

        # Save the game state
        save_game()


# Function to connect to the network
def connect():
    if has_item("EnigmaLink"):
        print_slow(Fore.GREEN + "Connecting to Enigma Corps network using EnigmaLink..." + Style.RESET_ALL)
        print_slow(Fore.GREEN + "Establishing connection...")
        time.sleep(1)
        print_slow(Fore.GREEN + "Linking EnigmaLink to remote server...")
        time.sleep(2)
        print_slow(Fore.GREEN + "Decrypting server security protocols...")
        time.sleep(3)
        print_slow(Fore.GREEN + "Bypassing firewall...")
        time.sleep(2)
        print_slow(Fore.GREEN + "Connection established!")
        print_slow(Fore.GREEN + "You are now connected to Enigma Corps network.")

        # Network command loop
        while True:
            command = input(Fore.GREEN + "> " + Style.RESET_ALL)

            # Scan the network for systems and vulnerabilities
            if command.lower() == "scan":
                scan()
            # Hack into a system or vulnerability
            elif command.lower().startswith("hack "):
                target = command[5:]
                hack(target)
            # Display connect help message
            elif command.lower() == "help":
                connect_help()
            # Exit the network
            elif command.lower() == "exit":
                print_slow("Disconnecting...")
                time.sleep(2)
                print_slow("Connection terminated.")
                break
            else:
                print_slow("Invalid command, please try again.")
    else:
        print_slow(
            Fore.RED + "You need to purchase EnigmaLink from the shop to connect to Enigma Corps network." + Style.RESET_ALL)


# Function to access the mail system
def mail():
    print_slow(Fore.LIGHTBLUE_EX + "Mail System:" + Style.RESET_ALL)

    while True:
        command = input(
            Fore.LIGHTBLUE_EX + "\n> " + Style.RESET_ALL)

        if command.lower() == 'l':
            # List emails
            list_emails(emails)
        elif command.lower().startswith('r '):
            # Read email
            subject = command[2:]
            read_email(emails, subject)
        elif command.lower() == 'help':
            # Display mail help message
            mail_help()
        elif command.lower() == 'exit':
            # Exit mail system
            print_slow(Fore.LIGHTBLUE_EX + "\nExiting Mail System..." + Style.RESET_ALL)
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


# Function to list emails
def list_emails(emails):
    print_slow(Fore.LIGHTBLUE_EX + "\nEmails:" + Style.RESET_ALL)

    for i, email in enumerate(emails):
        print_slow(Fore.LIGHTBLUE_EX + f"\n{email['subject']} - From: {email['sender']}" + Style.RESET_ALL)


# List of all systems in the game
all_systems = [
    {"name": "Amy", "type": "Computer", "level": 1, "password": "sexinthecity"},
    {"name": "Markus", "type": "Computer", "level": 1, "password": "12345"},
    {"name": "Billy", "type": "Computer", "level": 1, "password": "football"},
    {"name": "Camera1", "type": "Camera", "level": 2, "password": "camera1"},
    {"name": "Camera2", "type": "Camera", "level": 2, "password": "camera2"},
    {"name": "Server", "type": "Computer", "level": 3, "password": "server123"}
]

# Current player level
player_level = 1


def amy_system_command_loop(system):
    print_slow(Fore.YELLOW + "Connected to Amy's system." + Style.RESET_ALL)

    while True:
        command = input(Fore.YELLOW + "> " + Style.RESET_ALL)

        if command.lower() == "l":
            system.list_files()
        elif command.lower().startswith("r "):
            file_name = command[2:]
            system.read_file(file_name)
        elif command.lower() == "mail":
            amy_mail()
        elif command.lower() == "disconnect":
            print_slow(Fore.YELLOW + "\nDisconnecting from system...")
            print("")
            time.sleep(1)
            print_slow(Fore.YELLOW + "\nDisconnected ")
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


# Function to access Amy's mail system
def amy_mail():
    print_slow(Fore.LIGHTBLUE_EX + "Amy's Mail System:" + Style.RESET_ALL)

    while True:
        command = input(
            Fore.LIGHTBLUE_EX + "\n> " + Style.RESET_ALL)

        if command.lower() == 'l':
            # List emails
            list_emails(amy_system.emails)
        elif command.lower().startswith('r '):
            # Read email
            subject = command[2:]
            read_email(amy_system.emails, subject)
        elif command.lower() == 'help':
            # Display mail help message
            mail_help()
        elif command.lower() == 'exit':
            # Exit mail system
            print_slow(Fore.LIGHTBLUE_EX + "\nExiting Mail System..." + Style.RESET_ALL)
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


def hack(system_name):
    # Find the system in the all_systems list
    system = next((s for s in all_systems if s['name'].lower() == system_name.lower()), None)
    if system:
        if system['level'] <= player_level:
            # Prompt the user for the password
            password = input("Enter password: ")
            if password == system['password']:
                print_slow(Fore.GREEN + "Access granted!" + Style.RESET_ALL)
                if system['name'] == 'Amy':
                    amy_system_command_loop(amy_system)
                else:
                    # TODO: Implement other system interactions
                    pass
            else:
                print_slow(Fore.RED + "Access denied! Incorrect password." + Style.RESET_ALL)
        else:
            print_slow(Fore.RED + "Access denied! This system is locked." + Style.RESET_ALL)
    else:
        print_slow(Fore.RED + "System not found! Please try again." + Style.RESET_ALL)


def scan():
    print_slow(Fore.YELLOW + "Scanning network..." + Style.RESET_ALL)
    time.sleep(2)

    print_slow(Fore.YELLOW + "\nAvailable Systems:" + Style.RESET_ALL)
    for system in all_systems:
        if system['level'] <= player_level:
            print_slow(f"{system['name']} ({system['type']})")


# Function to display help message
def help_user():
    print_slow(Fore.MAGENTA + "Help:" + Style.RESET_ALL)
    print("")
    print_slow("[connect] - Use the 'connect' command to hack into Enigma Corps network.")
    print("")
    print_slow("[mail] - Use the 'mail' command to view and respond to emails from your client and other characters.")
    print("")
    print_slow("[balance] - Use the 'balance' command to view your current earnings which you can spend on upgrades. ")
    print("")
    print_slow("[shop] - Use the 'shop' command to view upgrades available in the shop. ")
    print("")
    print_slow("[help] - Use the 'help' command if you need assistance at any time.")
    print("")
    print_slow("[exit] - Use the 'exit' command to return to the Main Menu.")


def mail_help():
    print_slow(Fore.LIGHTBLUE_EX + "Mail Help:" + Style.RESET_ALL)
    print("")
    print_slow("[l] - Use the 'l' command to list all emails.")
    print("")
    print_slow("[r] - Use the 'r [subject]' command to read an email with the specified subject.")
    print("")
    print_slow("[exit] - Use the 'exit' command to return to the main terminal.")


def shop_help():
    print_slow(Fore.YELLOW + "Shop Help:" + Style.RESET_ALL)
    print("")
    print_slow("[buy] - Use the 'buy [upgrade]' command to purchase the upgrade in the shop. ")
    print("")
    print_slow("[exit] - Use the 'exit' command to return to the main terminal.")


def system_help():
    print("")
    print("[mail] - Use the 'mail' command to log into the users emails.")
    print("")
    print_slow("[l] - Use the 'l' command to list files in a users system.")
    print("")
    print_slow("[r] - Use the 'r [file]' command to read files in a users system")


def connect_help():
    print_slow(Fore.MAGENTA + "Connect Help:" + Style.RESET_ALL)
    print_slow(
        "[scan] - Use the 'scan' command to scan the network and search for available systems and vulnerabilities.")
    print("")
    print_slow("[hack] - Use the 'hack [system/vulnerability]' to hack into different systems.")
    print("")
    print_slow("[disconnect] - Use the 'disconnect' command to disconnect from the current system or vulnerability.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
