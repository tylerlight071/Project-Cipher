import random
import time

from colorama import Fore, Style
from components.common_functions import print_slow, clear_terminal


def generate_ports(num_ports):
    open_ports = set(random.sample(range(1, num_ports + 1), random.randint(1, num_ports // 2)))
    closed_ports = set(range(1, num_ports + 1)) - open_ports
    return open_ports, closed_ports


def port_scanning():
    num_ports = 10
    open_ports, closed_ports = generate_ports(num_ports)
    attempts = 5
    correct_guesses = 0
    scan_attempts = 2

    print_slow("Welcome to the Port Scanning minigame!")
    print_slow("")
    print_slow(f"Find the open ports in the range 1-{num_ports}.")
    print_slow("")
    print_slow(f"You have {attempts} attempts.")
    print_slow("")

    while scan_attempts > 0:
        print_slow("")
        print_slow(f"\nYou have {scan_attempts} scan attempts left.")
        print_slow("")
        start = int(input("Enter the start of the range to scan: "))
        print_slow("")
        end = int(input("Enter the end of the range to scan: "))
        print_slow("")

        num_open_ports_in_range = len(open_ports.intersection(range(start, end + 1)))
        print_slow("")
        print_slow(f"There are {num_open_ports_in_range} open ports in the range {start}-{end}.")

        scan_attempts -= 1

    while attempts > 0 and len(open_ports) > 0:
        port = int(input("\nEnter a port number to guess: "))

        if port in open_ports:
            print_slow(Fore.GREEN + "Port is open!" + Style.RESET_ALL)
            open_ports.remove(port)
            correct_guesses += 1
        elif port in closed_ports:
            print_slow(Fore.RED + "Port is closed." + Style.RESET_ALL)
            closed_ports.remove(port)
        else:
            print_slow("Invalid port number. Please enter a number between 1 and", num_ports)

        attempts -= 1

    if len(open_ports) == 0:
        print_slow(
            Fore.GREEN + "\nCongratulations! You have successfully found all the open ports and gained access to the camera." + Style.RESET_ALL)
        time.sleep(2)
        clear_terminal()
    else:
        print_slow(
            Fore.RED + f"\nHack Failed! You found {correct_guesses} out of {len(open_ports) + correct_guesses} open ports." + Style.RESET_ALL)
        time.sleep(1)
        clear_terminal()
        port_scanning()




