from components.common_functions import print_slow, clear_terminal, print_box
from ascii_art.ascii_art import sender_art
from colorama import Fore, Style


def first_call():
    clear_terminal()
    print(sender_art)
    print()
    print()
    print_box("Anonymous")
    print()
    print_slow(Fore.YELLOW + "That's a good start, but we already have that information.")
    print_slow("Regardless, I've transferred £20 into the account for your troubles.")
    print_slow("Keep digging Cipher!" + Style.RESET_ALL)
    input("Press [Enter] to continue: ")
    clear_terminal()


def second_call():
    clear_terminal()
    print(sender_art)
    print()
    print()
    print_box("Anonymous")
    print()
    print_slow(
        Fore.YELLOW + "Hey Cipher, you nailed it! 'Billy' just spilled the beans about wanting to climb the corporate ladder into management.")
    print_slow(
        "This is gold for us. We can guide 'Billy' toward training and workshops that align with our interests, nudging things in our favor.")
    print_slow(
        "Picture it – we're pulling the strings, helping 'Billy' grow, and steering the ship where we want it to go.")
    print_slow("Keep the ball rolling, Cipher!" + Style.RESET_ALL)
    input("Press [Enter] to continue: ")
    clear_terminal()
