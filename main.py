import msvcrt
import os
import pickle
import time
import colorama

from colorama import Fore, Style

from components.common_functions import clear_terminal, print_slow, shop_help, help_user, connect_help, mail_help, \
    system_help
from conversations.calls import intro_call, first_call, second_call, third_call, fourth_call, fifth_call
from conversations.minigame_calls import code_shatter_call
from minigames.code_shatter_minigame import code_shatter_minigame
from systems.level_1.amy.amy_system import AmySystem
from systems.level_1.billy.billy_system import BillySystem
from systems.level_1.markus.markus_system import MarkusSystem

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
has_intro_call = False
evidence = []
amy_system = AmySystem()
billy_system = BillySystem()
markus_system = MarkusSystem()
bg_music_enabled = True
player_level = 1


# Save the game state to a file
def save_game():
    global inventory, balance, emails, has_read_email, evidence, player_level, has_intro_call  # Add has_read_email here
    with open('savegame.pkl', 'wb') as f:
        pickle.dump((inventory, balance, emails, has_read_email, evidence, player_level, has_intro_call),
                    f)

    # Load the game state from a file


def load_game():
    global inventory, balance, emails, has_read_email, evidence, player_level, has_intro_call
    if os.path.exists('savegame.pkl'):
        with open('savegame.pkl', 'rb') as f:
            inventory, balance, emails, has_read_email, evidence, player_level, has_intro_call = pickle.load(f)
    else:
        # If the savegame file doesn't exist, set the default values
        inventory = []
        player_level = 1
        evidence = []
        has_intro_call = False
        balance = 30000
        emails = [
            {
                "sender": "Hacker's Digest",
                "subject": "Weekly Hacker's Digest",
                "body": (
                    "Issue #143\n\n"
                    "Cipher,\n\n"
                    "Welcome to the latest edition of Hacker's Digest! In this issue: \n\n"
                    "- Unveiling the Latest Exploits\n"
                    "- Spotlight on Cryptocurrency Security\n"
                    "- Interview with a Grey Hat Hacker\n"
                    "- Tool of the Week: EnigmaLink\n\n"
                    "Don't miss out on the latest in the world of hacking and cybersecurity. Stay informed and stay secure!\n\n"
                    "Best regards,\n"
                    "Hacker's Digest Team"
                )
            },
            {
                "sender": "The Cyber Mythbuster",
                "subject": "Busting Cybersecurity Myths",
                "body": (
                    "Cipher,\n\n"
                    "Heard any wild cybersecurity myths lately? This week, we're busting the craziest ones, including:\n\n"
                    "- Using 'Password123' for Maximum Security\n"
                    "- Cyber Ninjas and Their Stealthy VPNs\n"
                    "- USB Drives: The Fountain of Eternal Data\n\n"
                    "Stay myth-free and keep on hacking (responsibly)!\n\n"
                    "Mythbustingly,\n"
                    "The Cyber Mythbuster"
                )
            },
            {
                "sender": "CyberSilliness",
                "subject": "Where Cyber Meets Comedy",
                "body": (
                    "Welcome to the CyberSilliness Gazette\n"
                    "Where we believe that a good laugh is the ultimate antivirus! In this week's hilarity-packed issue:\n\n"
                    "- Cyber Jokes to Crack You Up (Without Cracking Your Passwords)\n"
                    "- Tech Support Horror Stories: A Comedy of Errors\n"
                    "- Chuckle Challenge: Share Your Funniest Cybersecurity Anecdote\n"
                    "- Meet the Cyber Clowns: Our Team's Silly Security Habits Revealed\n\n"
                    "Laughter is contagious, and so is good cybersecurity. Dive into the giggles and stay safe!\n\n"
                    "Silly Regards,\n"
                    "The CyberSilliness Team"
                )
            },
            {
                "sender": "Security Insight Weekly",
                "subject": "Navigating the Cybersecurity Landscape",
                "body": (
                    "Hello Cipher,\n\n"
                    "Welcome to Security Insight Weekly, your reliable source for navigating the ever-evolving cybersecurity landscape. In this week's issue:\n\n"
                    "- Threat Analysis: Understanding Recent Cybersecurity Incidents\n"
                    "- Best Practices for Endpoint Security\n"
                    "- Industry Spotlight: Healthcare Cybersecurity Challenges\n"
                    "- Security Compliance Update: Staying Aligned with Regulations\n\n"
                    "Stay informed and empowered as we delve into the serious aspects of cybersecurity. Your security is our priority.\n\n"
                    "Best regards,\n"
                    "The Security Insight Team"
                )
            },
        ]


# New function for game settings
def game_settings():
    global bg_music_enabled

    print_slow(Fore.GREEN + "░██████╗███████╗████████╗████████╗██╗███╗░░██╗░██████╗░░██████╗")
    print_slow(Fore.GREEN + "██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗░██║██╔════╝░██╔════╝")
    print_slow(Fore.GREEN + "╚█████╗░█████╗░░░░░██║░░░░░░██║░░░██║██╔██╗██║██║░░██╗░╚█████╗░")
    print_slow(Fore.GREEN + "░╚═══██╗██╔══╝░░░░░██║░░░░░░██║░░░██║██║╚████║██║░░╚██╗░╚═══██╗")
    print_slow(Fore.GREEN + "██████╔╝███████╗░░░██║░░░░░░██║░░░██║██║░╚███║╚██████╔╝██████╔╝")
    print_slow(Fore.GREEN + "╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═════╝░" + Style.RESET_ALL)
    print_slow("")
    print_slow("")
    print_slow("")
    print_slow(Fore.GREEN + " --------------------------------------------" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "|                                            |" + Style.RESET_ALL)
    print_slow(
        Fore.GREEN + f"|  [Background Music]   {'Enabled              |' if bg_music_enabled else 'Disabled           |'}" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "|  [Delete Savegame]                         |" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "|                                            |" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "|  [Back to Main Menu]                       |" + Style.RESET_ALL)
    print_slow(Fore.GREEN + " --------------------------------------------" + Style.RESET_ALL)

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
        confirm = input(Fore.RED + "\nAre you sure you want to delete the savegame? (yes/no): " + Style.RESET_ALL)
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


def remove_from_inventory(item):
    if item in inventory:
        inventory.remove(item)


def add_evidence(evidence_item):
    evidence.append(evidence_item)


def has_evidence(evidence_item):
    return evidence_item in evidence


# Prints the games title
def main():
    clear_terminal()
    colorama.init()
    print_slow(Fore.GREEN + "██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░██╗░█████╗░████████╗" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔══██╗╚══██╔══╝" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░███████║███████║░░░██║░░░" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔══██║██╔══██║░░░██║░░░" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗██║░░██║██║░░██║░░░██║░░░" + Style.RESET_ALL)
    print_slow(Fore.GREEN + "╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░" + Style.RESET_ALL)

    # Pause for 2 seconds before clearing the console
    time.sleep(5)

    # Clear the console
    clear_terminal()

    # Main menu loop
    while True:
        print_slow(Fore.GREEN + "███╗░░░███╗░█████╗░██╗███╗░░██╗  ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
        print_slow(Fore.GREEN + "████╗░████║██╔══██╗██║████╗░██║  ████╗░████║██╔════╝████╗░██║██║░░░██║")
        print_slow(Fore.GREEN + "██╔████╔██║███████║██║██╔██╗██║  ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
        print_slow(Fore.GREEN + "██║╚██╔╝██║██╔══██║██║██║╚████║  ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
        print_slow(Fore.GREEN + "██║░╚═╝░██║██║░░██║██║██║░╚███║  ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
        print_slow(
            Fore.GREEN + "╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░" + Style.RESET_ALL)
        print_slow("")
        print_slow("")
        print_slow("")
        print_slow(Fore.GREEN + " --------------------------------------------" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Start]  Start the game                    |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "|                                            |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Options] Change the settings              |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "|                                            |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + "| [Exit]   Exit the game                     |" + Style.RESET_ALL)
        print_slow(Fore.GREEN + " --------------------------------------------" + Style.RESET_ALL)

        choice = input(Fore.GREEN + "\n> " + Style.RESET_ALL)

        # Start the game
        if choice.lower() == "start":
            load_game()
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
            time.sleep(2)
            clear_terminal()


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
    print_slow(f"Your current balance is: £{get_balance()}")


# Function to read files and marks files as evidence
def read_file(file_content, file_name):
    global has_read_file, evidence
    global balance

    # Print the file content
    print_slow(Fore.LIGHTBLUE_EX + f"\n{file_name}:\n\n{file_content}" + Style.RESET_ALL)
    print_slow("")

    # Check if the file is one of the specific files that increases evidence count
    if file_name.lower() in ["employee_performance_review.txt"]:
        evidence_item = 4
        if not has_evidence(evidence_item):
            print_slow("Adding evidence to the list...")
            print_slow("")
            print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
            add_evidence(evidence_item)
            print_slow("")
            print_slow("")
            time.sleep(3)
            print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
            input(Fore.GREEN + "> " + Style.RESET_ALL)
            fourth_call()

    if file_name.lower() in ["meeting_minutes.txt"]:
        evidence_item = 5
        if not has_evidence(evidence_item):
            print_slow("Adding evidence to the list...")
            print_slow("")
            print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
            add_evidence(evidence_item)
            print_slow("")
            print_slow("")
            time.sleep(3)
            print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
            input(Fore.GREEN + "> " + Style.RESET_ALL)
            fifth_call()
    # Add more file names here as needed

    # Add money to balance based on the file name
    if file_name.lower() == "employee_performance_review.txt":
        balance += 30
    elif file_name.lower() == "meeting_minutes.txt":
        balance += 50


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
    clear_terminal()
    print_slow(Fore.YELLOW + r'''    ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░  ███╗░░░███╗░█████╗░██████╗░██╗░░██╗███████╗████████╗
    ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝
    ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝  ██╔████╔██║███████║██████╔╝█████═╝░█████╗░░░░░██║░░░
    ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░██╔══╝░░░░░██║░░░
    ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║  ██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗███████╗░░░██║░░░
    ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░''' + Style.RESET_ALL)

    print_slow(Fore.YELLOW + "\nWelcome to the Hacker's Market!" + Style.RESET_ALL)
    print_slow("")
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
            time.sleep(1)
            clear_terminal()
            break
        elif command.lower() == 'help':
            shop_help()
        elif command.lower().startswith('buy '):
            upgrade_name = command[4:]
            for upgrade in upgrades:
                if upgrade_name.lower() == upgrade['name'].lower():
                    if get_balance() >= upgrade['price']:
                        print_slow("")
                        print_slow(
                            Fore.GREEN + f"You have successfully purchased {upgrade['name']} for ${upgrade['price']}!" + Style.RESET_ALL)
                        subtract_money(upgrade['price'])
                        print_slow("")
                        print_balance()
                        add_to_inventory(upgrade['name'])
                        time.sleep(2)
                        clear_terminal()
                        shop()

                        # Check if the purchased upgrade is CodeShatter
                        if upgrade_name.lower() == 'codeshatter':
                            print_slow("")
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
    global has_intro_call
    print_slow("\nStarting game...")
    time.sleep(1)
    print_slow("\nLoading assets...")
    time.sleep(1)
    clear_terminal()

    if has_intro_call:
        pass
    else:
        print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
        input(Fore.GREEN + "> " + Style.RESET_ALL)
        intro_call()
        has_intro_call = True
        pass

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
        elif command.lower() == "remove":
            remove_from_inventory(item="CodeShatter")
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
    print_slow("")
    print_slow(Fore.YELLOW + "Scanning network..." + Style.RESET_ALL)
    time.sleep(2)
    print_slow("")

    print_slow(Fore.YELLOW + "\nAvailable Systems:" + Style.RESET_ALL)
    print_slow("")
    for system in all_systems:
        if system['level'] <= player_level:
            print_slow("")
            print_slow(f"{system['name']} ({system['type']})")
            print_slow("")


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
                print_slow("")
                password = getpass_star("Enter password: ")
                print_slow("")
                if password == system['password']:
                    print_slow("")
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
                    print_slow("")
                    print_slow(Fore.RED + "Access denied! Incorrect password." + Style.RESET_ALL)

        else:
            print_slow("")
            print_slow(Fore.RED + "Access denied! This system is locked." + Style.RESET_ALL)
    else:
        print_slow("")
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
            print_slow(
                Fore.LIGHTBLUE_EX + f"\nFrom: {email['sender']}\nSubject: {email['subject']}\n\n{email['body']}" + Style.RESET_ALL)

            # Check if the email is one of the specific emails that increases evidence count
            if email['subject'].lower() in ["project update"]:
                evidence_item = 3
                if not has_evidence(evidence_item):
                    print_slow("Adding evidence to the list...")
                    print_slow("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
                    add_evidence(evidence_item)
                    print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
                    input(Fore.GREEN + "> " + Style.RESET_ALL)
                    third_call()

            if email['subject'].lower() in ["professional development"]:
                evidence_item = 2
                if not has_evidence(evidence_item):
                    print_slow("Adding evidence to the list...")
                    print_slow("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
                    add_evidence(evidence_item)
                    print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
                    input(Fore.GREEN + "> " + Style.RESET_ALL)
                    second_call()

            if email['subject'].lower() == "can't stop thinking about you" and email['sender'].lower() == 'amy':
                evidence_item = 1
                if not has_evidence(evidence_item):
                    print_slow("Adding evidence to the list...")
                    print_slow("")
                    print_slow("")
                    print_slow(Fore.GREEN + "Evidence Secured" + Style.RESET_ALL)
                    add_evidence(evidence_item)
                    print_slow(Fore.GREEN + "Incoming Call..." + Style.RESET_ALL)
                    input(Fore.GREEN + "> " + Style.RESET_ALL)
                    first_call()
            if email['subject'].lower() == "upcoming software update" and email['sender'].lower() == 'markus':
                evidence_item = 6
                if not has_evidence(evidence_item):
                    print_slow("Adding evidence to the list...")
                    print_slow("")
                    print_slow("")
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

    if not email_found:
        print_slow(Fore.RED + "\nNo email found with that subject, please try again." + Style.RESET_ALL)


def connect():
    if has_item("EnigmaLink"):
        print_slow("")
        print_slow(Fore.GREEN + "Connecting to Enigma Corps network using EnigmaLink..." + Style.RESET_ALL)
        time.sleep(0.5)
        print_slow("")
        print_slow(Fore.GREEN + "Establishing connection...")
        time.sleep(1)
        print_slow("")
        print_slow(Fore.GREEN + "Linking EnigmaLink to remote server...")
        time.sleep(2)
        print_slow("")
        print_slow(Fore.GREEN + "Decrypting server security protocols...")
        time.sleep(3)
        print_slow("")
        print_slow(Fore.GREEN + "Bypassing firewall...")
        time.sleep(2)
        print_slow("")
        print_slow(Fore.GREEN + "Connection established!")
        time.sleep(2)
        print_slow("")
        print_slow(Fore.GREEN + "You are now connected to Enigma Corps network.")
        print_slow("")

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
                print_slow("")
                print_slow("Connection terminated.")
                print_slow("")
                break
            else:
                print_slow("Invalid command, please try again.")
    else:
        print_slow(
            Fore.RED + "You need to purchase EnigmaLink from the shop to connect to Enigma Corps network." + Style.RESET_ALL)


def mail():
    print_slow("")
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
            print_slow("")
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
    print_slow("")
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
        elif command.lower() == "clear":
            clear_terminal()
        elif command.lower() == "help":
            system_help()
        elif command.lower() == "disconnect":
            print_slow(Fore.YELLOW + "\nDisconnecting from system...")
            print_slow("")
            time.sleep(1)
            print_slow(Fore.YELLOW + "\nDisconnected ")
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


# Function to access Amy's mail system
def amy_mail():
    print_slow("")
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
        elif command.lower() == 'clear':
            clear_terminal()
        elif command.lower() == 'exit':
            # Exit mail system
            print_slow(Fore.LIGHTBLUE_EX + "\nExiting Mail System..." + Style.RESET_ALL)
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


def billy_system_command_loop(system):
    print_slow("")
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
        elif command.lower() == "clear":
            clear_terminal()
        elif command.lower() == "disconnect":
            print_slow(Fore.YELLOW + "\nDisconnecting from system...")
            print_slow("")
            time.sleep(1)
            print_slow(Fore.YELLOW + "\nDisconnected ")
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


def billy_mail():
    print_slow("")
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
    print_slow("")
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
            print_slow("")
            time.sleep(1)
            print_slow(Fore.YELLOW + "\nDisconnected ")
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)


# Function to access Amy's mail system
def markus_mail():
    print_slow("")
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
