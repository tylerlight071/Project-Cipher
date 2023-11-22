from components.common_functions import print_slow, clear_terminal, print_box
from ascii_art.ascii_art import sender_art
from colorama import Fore, Style


def code_shatter_call():
    clear_terminal()
    print_slow(sender_art)
    print_slow("")
    print_slow("")
    print_box("Anonymous")
    print_slow("")
    print_slow(Fore.YELLOW + "I see you have bought CodeShatter!")
    print_slow("This item is a one time use upgrade so once you get the password, it is gone so use wisely!")
    print_slow("But don't threat, if you fail, you get a chance to retry. The item is only used when you get the password, so be sure to write it down!" + Style.RESET_ALL)
    input("Press [Enter] to continue: ")
    clear_terminal()
