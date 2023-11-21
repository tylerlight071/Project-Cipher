import msvcrt
import os
import pickle
import colorama
from colorama import Fore, Style
import time
import subprocess

from components.help.help import system_help, shop_help, mail_help, help_user, connect_help
from components.print_slow.print_slow import print_slow
from conversations.calls import first_call, second_call
from conversations.minigame_calls import code_shatter_call
from minigames.code_shatter_minigame import code_shatter_minigame
from components.common_functions import clear_terminal

from systems.level_1.markus.markus_system import MarkusSystem
from systems.level_1.billy.billy_system import BillySystem
from systems.level_1.amy.amy_system import AmySystem

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
has_read_file = False
evidence = []
amy_system = AmySystem()
billy_system = BillySystem()
markus_system = MarkusSystem()
bg_music_enabled = True
player_level = 1


# Save the game state to a file
def save_game():
    global inventory, balance, emails, has_read_email, evidence, player_level  # Add has_read_email here
    with open('savegame.pkl', 'wb') as f:
        pickle.dump((inventory, balance, emails, has_read_email, evidence, player_level),
                    f)

    # Load the game state from a file


def load_game():
    global inventory, balance, emails, has_read_email, evidence, player_level
    if os.path.exists('savegame.pkl'):
        with open('savegame.pkl', 'rb') as f:
            inventory, balance, emails, has_read_email, evidence, player_level = pickle.load(f)
    else:
        # If the savegame file doesn't exist, set the default values
        inventory = []
        player_level = 1
        evidence = []
        balance = 30000
        emails = [
            {
                "sender": "Prophet",
                "subject": "Operation Enigma",
                "body": (
                    "Cipher,\n\n"
                    "Welcome to the resistance. This communication serves as your official contract initiation for Operation Enigma, a clandestine mission against Enigma Corp.\n\n"
                    "Your unique skills have been identified and selected for this critical operation. Your objective is to expose the secrets of Enigma Corp and hold them accountable for their actions.\n\n"
                    "Your first task under this contract is to acquire a specialized tool known as 'EnigmaLink' from the Hacker's Market. "
                    "This application contains a hidden backdoor, strategically planted by our operatives, which will grant you access to Enigma Corps servers.\n\n"
                    "Once you have secured EnigmaLink, initiate your infiltration by using the 'connect' command. "
                    "Your mission is to navigate through the network, collecting any valuable intelligence that could be crucial to our cause.\n\n"
                    "Begin your investigation with an employee named Amy. We have managed to obtain her password through unconventional means. "
                    "Use 'sexinthecity' to access her computer and gather any pertinent information.\n\n"
                    "All collected data is considered highly confidential and vital to the success of this operation. "
                    "You are expected to be thorough and meticulous in your investigation.\n\n"
                    "This contract is binding, and your success is paramount. The future of our operation and cause rests upon your shoulders. Execute with precision and diligence.\n\n"
                    "Best of luck, Cipher.\n"
                    "May the odds be in your favor."
                )
            },
        ]


# New function for game settings
def game_settings():
    global bg_music_enabled
    print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "|                 Game Settings              |" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
    print_slow(
        Fore.GREEN + f"| 1. Background Music     {'Enabled            |' if bg_music_enabled else 'Disabled           |'}" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "| 2. Delete Savegame                         |" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "| 3. Back to Main Menu                       |" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)

    choice = input(Fore.GREEN + "\n> " + Style.RESET_ALL)

    if choice.lower() == "background music":
        # Toggle background music
        bg_music_enabled = not bg_music_enabled
        if bg_music_enabled:
            pygame.mixer.music.play(-1)
            print_slow(Fore.GREEN + "\nBackground Music Enabled" + Style.RESET_ALL)
            time.sleep(1)
            clear_terminal()
            game_settings()
        else:
            pygame.mixer.music.stop()
            print_slow(Fore.RED + "\nBackground Music Disabled" + Style.RESET_ALL)
            time.sleep(1)
            clear_terminal()
            game_settings()
    elif choice.lower() == "delete savegame":
        # Delete savegame
        confirm = input("\nAre you sure you want to delete the savegame? (yes/no): ")
        if confirm.lower() == "yes":
            try:
                os.remove("savegame.pkl")
                print_slow(Fore.GREEN + "\nSavegame Deleted" + Style.RESET_ALL)
                time.sleep(1)
                clear_terminal()
                game_settings()
            except FileNotFoundError:
                print_slow(Fore.RED + "\nSavegame not found" + Style.RESET_ALL)
                time.sleep(1)
                clear_terminal()
                game_settings()
    elif choice.lower() == "exit" or choice.lower() == "back to main menu":
        # Return to Main Menu
        print_slow(Fore.GREEN + "\nReturning to Main Menu..." + Style.RESET_ALL)
        time.sleep(1)
        clear_terminal()
    else:
        print_slow(Fore.RED + "\nInvalid choice, please try again." + Style.RESET_ALL)
        time.sleep(1)
        clear_terminal()
        game_settings()


# Function to add an item to the inventory
def add_to_inventory(item):
    inventory.append(item)


def add_evidence(evidence_item):
    evidence.append(evidence_item)


def has_evidence(evidence_item):
    return evidence_item in evidence


# Prints the games title
def main():
    clear_terminal()
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
    clear_terminal()

    load_game()

    # Main menu loop
    while True:
        print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "|                 Main Menu                  |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Start]  Start the game                    |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Options] Change the settings              |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Exit]   Exit the game                     |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "---------------------------------------------" + Style.RESET_ALL)

        choice = input(Fore.GREEN + "\n> " + Style.RESET_ALL)

        # Start the game
        if choice.lower() == "start":
            start_game()
        # Open game settings
        elif choice.lower() == "options":
            clear_terminal()
            game_settings()
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


def add_level(level):
    global player_level
    player_level += level


# Function to print the user's balance
def print_balance():
    print(f"Your current balance is: £{get_balance()}")


# Function to read files and marks files as evidence
def read_file(file_content, file_name):
    global has_read_file, evidence
    global balance

    # Print the file content
    print_slow(Fore.LIGHTBLUE_EX + f"\n{file_name}:\n\n{file_content}" + Style.RESET_ALL)

    # Check if the file is one of the specific files that increases evidence count
    if file_name.lower() in ["employee_performance_review.txt"]:
        evidence_item = 4
        if not has_evidence(evidence_item):
            add_evidence(evidence_item)
            print("Adding evidence to the list...")
            print("")
            print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)

    if file_name.lower() in ["meeting_minutes.txt"]:
        evidence_item = 5
        if not has_evidence(evidence_item):
            add_evidence(evidence_item)
            print("Adding evidence to the list...")
            print("")
            print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)

    # Add more file names here as needed

    # Add money to balance based on the file name
    if file_name.lower() == "employee_performance_review.txt":
        balance += 30
    elif file_name.lower() == "meeting_minutes.txt":
        balance += 50

    # Print the updated balance
    print_balance()


# List of available upgrades
upgrades = [
    {"name": "EnigmaLink", "description": "Application required to connect to Enigma Corps network.", "price": 300},
    {"name": "CodeShatter", "description": "A powerful password breaker that can crack even the strongest passwords.",
     "price": 200},
    {"name": "EyeSpy", "description": "A privacy breaker to gain access to the smallest of cameras.", "price": 500},
    {"name": "Rift", "description": "Break the barrier between the Server and Network.", "price": 800}
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
    print("")
    print_slow(Fore.YELLOW + "Here you can buy upgrades to improve your hacking abilities.\n" + Style.RESET_ALL)

    while True:
        # Display the list of available upgrades
        for i, upgrade in enumerate(upgrades):
            print_slow(
                Fore.YELLOW + f"\n{upgrade['name']} - {upgrade['description']} - £{upgrade['price']}" + Style.RESET_ALL)

        # Get the user's choice
        command = input(Fore.YELLOW + "\n> " + Style.RESET_ALL)

        # Buy the chosen upgrade
        if command.lower() == 'exit':
            print_slow(Fore.YELLOW + "\nExiting Hacker's Market" + Style.RESET_ALL)
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

                        # Check if the purchased upgrade is CodeShatter
                        if upgrade_name.lower() == 'codeshatter':
                            print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
                            input(Fore.GREEN + "> " + Style.RESET_ALL)
                            code_shatter_call()

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
    clear_terminal()
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
        # Enter shop
        elif command.lower() == "shop":
            shop()
        # Clear terminal
        elif command.lower() == "clear":
            clear_terminal()
        # Return to the main menu
        elif command.lower() == "exit":
            print_slow("Returning to Main Menu...")
            break
        else:
            print_slow("Invalid command, please try again.")

        # Save the game state
        save_game()


# Function to check if an item is in the inventory
def has_item(item):
    return item in inventory


def scan():
    print_slow(Fore.YELLOW + "Scanning network..." + Style.RESET_ALL)
    time.sleep(2)

    print_slow(Fore.YELLOW + "\nAvailable Systems:" + Style.RESET_ALL)
    for system in all_systems:
        if system['level'] <= player_level:
            print_slow(f"{system['name']} ({system['type']})")


def getpass_star(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = []
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            break
        elif char == '\b':  # Backspace
            if password:
                password.pop()
                print('\b \b', end='', flush=True)
        else:
            password.append(char)
            print('*', end='', flush=True)
    print()  # Move to the next line
    return ''.join(password)


def hack(system_name):
    # Find the system in the all_systems list
    system = next((s for s in all_systems if s['name'].lower() == system_name.lower()), None)
    if system:
        if system['level'] <= player_level:
            # Check for CodeShatter before prompting for password
            if system['name'] == 'Markus' and has_item("CodeShatter"):
                code_shatter_minigame()
                print_slow("Password Cracked: 735@&!//")
                input("Press [Enter] to continue")
                clear_terminal()
                markus_system_command_loop(markus_system)
                add_level(player_level)
            else:
                # Prompt the user for the password
                password = getpass_star("Enter password: ")
                if password == system['password']:
                    print_slow(Fore.GREEN + "Access granted!" + Style.RESET_ALL)
                    if system['name'] == 'Amy':
                        amy_system_command_loop(amy_system)
                    elif system['name'] == 'Billy':
                        billy_system_command_loop(billy_system)
                    elif system['name'] == 'Markus':
                        markus_system_command_loop(markus_system)
                        add_level(player_level)
                    else:
                        # Add more conditions for other systems
                        pass
                else:
                    print_slow(Fore.RED + "Access denied! Incorrect password." + Style.RESET_ALL)
        else:
            print_slow(Fore.RED + "Access denied! This system is locked." + Style.RESET_ALL)
    else:
        print_slow(Fore.RED + "System not found! Please try again." + Style.RESET_ALL)


def list_emails(emails):
    print_slow(Fore.LIGHTBLUE_EX + "\nEmails:" + Style.RESET_ALL)

    for i, email in enumerate(emails):
        print_slow(Fore.LIGHTBLUE_EX + f"\n{email['subject']} - From: {email['sender']}" + Style.RESET_ALL)


def read_email(emails, subject):
    global has_read_email, evidence
    global balance
    email_found = False
    for email in emails:
        if email['subject'].lower() == subject.lower():
            email_found = True
            # If the email is from Prophet, set has_read_email to True
            if email['sender'].lower() == 'prophet':
                has_read_email = True
            print_slow(
                Fore.LIGHTBLUE_EX + f"\nFrom: {email['sender']}\nSubject: {email['subject']}\n\n{email['body']}" + Style.RESET_ALL)

            # Check if the email is one of the specific emails that increases evidence count
            if email['subject'].lower() in ["project update"]:
                evidence_item = 3
                if not has_evidence(evidence_item):
                    add_evidence(evidence_item)
                    print("Adding evidence to the list...")
                    print("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)

            if email['subject'].lower() in ["professional development"]:
                evidence_item = 2
                if not has_evidence(evidence_item):
                    print("Adding evidence to the list...")
                    print("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
                    add_evidence(evidence_item)
                    print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
                    input(Fore.GREEN + "> " + Style.RESET_ALL)
                    second_call()

            if email['subject'].lower() == "can't stop thinking about you" and email['sender'].lower() == 'amy':
                evidence_item = 1
                if not has_evidence(evidence_item):
                    print("Adding evidence to the list...")
                    print("")
                    print("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
                    add_evidence(evidence_item)
                    print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
                    input(Fore.GREEN + "> " + Style.RESET_ALL)
                    first_call()
            if email['subject'].lower() == "upcoming software update" and email['sender'].lower() == 'markus':
                evidence_item = 6
                if not has_evidence(evidence_item):
                    print("Adding evidence to the list...")
                    print("")
                    print("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
                    add_evidence(evidence_item)

                    # Add money to balance based on the email subject
            if email['subject'].lower() == "professional development":
                balance += 30
            elif email['subject'].lower() == "project update":
                balance += 50
            elif email['subject'].lower() == "can't stop thinking about you":
                balance += 20
            elif email['subject'].lower() == "upcoming software update":
                balance += 50

            # Print the updated balance
            print_balance()

    if not email_found:
        print_slow(Fore.RED + "\nNo email found with that subject, please try again." + Style.RESET_ALL)


def connect():
    if has_item("EnigmaLink"):
        print_slow(Fore.GREEN + "Connecting to Enigma Corps network using EnigmaLink..." + Style.RESET_ALL)
        time.sleep(0.5)
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

# List of all systems in the game
all_systems = [
    {"name": "Amy", "type": "Computer", "level": 1, "password": "sexinthecity"},
    {"name": "Markus", "type": "Computer", "level": 1, "password": "735@&!//"},
    {"name": "Billy", "type": "Computer", "level": 1, "password": "football"},
    {"name": "Camera1", "type": "Camera", "level": 2, "password": "camera1"},
    {"name": "Camera2", "type": "Camera", "level": 2, "password": "camera2"},
    {"name": "Server", "type": "Computer", "level": 3, "password": "server123"}
]


def amy_system_command_loop(system):
    print_slow(Fore.YELLOW + "Connected to Amy's system." + Style.RESET_ALL)

    while True:
        command = input(Fore.YELLOW + "> " + Style.RESET_ALL)

        if command.lower() == "l":
            system.list_files()
        elif command.lower().startswith("r "):
            file_name = command[2:]
            file_content = system.read_file(file_name)  # Store the file content in a variable
            if file_content:  # Check if the file was found
                read_file(file_content, file_name)  # Pass the file content to the read_file function
        elif command.lower() == "mail":
            amy_mail()
        elif command.lower() == "help":
            system_help()
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


def billy_system_command_loop(system):
    print_slow(Fore.YELLOW + "Connected to Billy's system." + Style.RESET_ALL)

    while True:
        command = input(Fore.YELLOW + "> " + Style.RESET_ALL)

        if command.lower() == "l":
            system.list_files()
        elif command.lower().startswith("r "):
            file_name = command[2:]
            file_content = system.read_file(file_name)  # Store the file content in a variable
            if file_content:  # Check if the file was found
                read_file(file_content, file_name)  # Pass the file content to the read_file function
        elif command.lower() == "mail":
            billy_mail()
        elif command.lower() == "help":
            system_help()
        elif command.lower() == "disconnect":
            print_slow(Fore.YELLOW + "\nDisconnecting from system...")
            print("")
            time.sleep(1)
            print_slow(Fore.YELLOW + "\nDisconnected ")
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


def billy_mail():
    print_slow(Fore.LIGHTBLUE_EX + "Billy's Mail System:" + Style.RESET_ALL)

    while True:
        command = input(
            Fore.LIGHTBLUE_EX + "\n> " + Style.RESET_ALL)

        if command.lower() == 'l':
            # List emails
            list_emails(billy_system.emails)
        elif command.lower().startswith('r '):
            # Read email
            subject = command[2:]
            read_email(billy_system.emails, subject)
        elif command.lower() == 'help':
            # Display mail help message
            mail_help()
        elif command.lower() == 'exit':
            # Exit mail system
            print_slow(Fore.LIGHTBLUE_EX + "\nExiting Mail System..." + Style.RESET_ALL)
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


def markus_system_command_loop(system):
    print_slow(Fore.YELLOW + "Connected to Markus' system." + Style.RESET_ALL)

    while True:
        command = input(Fore.YELLOW + "> " + Style.RESET_ALL)

        if command.lower() == "l":
            system.list_files()
        elif command.lower().startswith("r "):
            file_name = command[2:]
            file_content = system.read_file(file_name)  # Store the file content in a variable
            if file_content:  # Check if the file was found
                read_file(file_content, file_name)  # Pass the file content to the read_file function
        elif command.lower() == "mail":
            markus_mail()
        elif command.lower() == "help":
            system_help()
        elif command.lower() == "disconnect":
            print_slow(Fore.YELLOW + "\nDisconnecting from system...")
            print("")
            time.sleep(1)
            print_slow(Fore.YELLOW + "\nDisconnected ")
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


# Function to access Amy's mail system
def markus_mail():
    print_slow(Fore.LIGHTBLUE_EX + "Markus' Mail System:" + Style.RESET_ALL)

    while True:
        command = input(
            Fore.LIGHTBLUE_EX + "\n> " + Style.RESET_ALL)

        if command.lower() == 'l':
            # List emails
            list_emails(markus_system.emails)
        elif command.lower().startswith('r '):
            # Read email
            subject = command[2:]
            read_email(markus_system.emails, subject)
        elif command.lower() == 'help':
            # Display mail help message
            mail_help()
        elif command.lower() == 'exit':
            # Exit mail system
            print_slow(Fore.LIGHTBLUE_EX + "\nExiting Mail System..." + Style.RESET_ALL)
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
