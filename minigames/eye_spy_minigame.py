import random
from colorama import Fore, Style

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

    print("Welcome to the Port Scanning minigame!")
    print("")
    print(f"Find the open ports in the range 1-{num_ports}.")
    print("")
    print(f"You have {attempts} attempts.")
    print("")

    while scan_attempts > 0:
        print("")
        print(f"\nYou have {scan_attempts} scan attempts left.")
        print("")
        start = int(input("Enter the start of the range to scan: "))
        print("")
        end = int(input("Enter the end of the range to scan: "))
        print("")

        num_open_ports_in_range = len(open_ports.intersection(range(start, end + 1)))
        print("")
        print(f"There are {num_open_ports_in_range} open ports in the range {start}-{end}.")

        scan_attempts -= 1

    while attempts > 0 and len(open_ports) > 0:
        port = int(input("\nEnter a port number to guess: "))

        if port in open_ports:
            print(Fore.GREEN + "Port is open!" + Style.RESET_ALL)
            open_ports.remove(port)
            correct_guesses += 1
        elif port in closed_ports:
            print(Fore.RED + "Port is closed." + Style.RESET_ALL)
            closed_ports.remove(port)
        else:
            print("Invalid port number. Please enter a number between 1 and", num_ports)

        attempts -= 1

    if len(open_ports) == 0:
        print(Fore.GREEN + "\nCongratulations! You have successfully found all the open ports and gained access to the camera." + Style.RESET_ALL)
    else:
        print(Fore.RED + f"\nGame Over! You found {correct_guesses} out of {len(open_ports) + correct_guesses} open ports." + Style.RESET_ALL)

port_scanning()