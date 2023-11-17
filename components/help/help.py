import time
from colorama import Fore, Style


# Makes the text have a delay of (x) when printed to screen
def print_slow(text, delay=0.00):  # change to 0.01
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


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
    print_slow("[clear] - Use the 'clear' command to clear the terminal.")
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
