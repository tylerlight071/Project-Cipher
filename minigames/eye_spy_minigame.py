import random

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
    print(f"Find the open ports in the range 1-{num_ports}. You have {attempts} attempts.")

    while scan_attempts > 0:
        print(f"\nYou have {scan_attempts} scan attempts left.")
        start = int(input("Enter the start of the range to scan: "))
        end = int(input("Enter the end of the range to scan: "))

        num_open_ports_in_range = len(open_ports.intersection(range(start, end + 1)))
        print(f"There are {num_open_ports_in_range} open ports in the range {start}-{end}.")

        scan_attempts -= 1

    while attempts > 0 and len(open_ports) > 0:
        port = int(input("\nEnter a port number to guess: "))

        if port in open_ports:
            print("Port is open!")
            open_ports.remove(port)
            correct_guesses += 1
        elif port in closed_ports:
            print("Port is closed.")
            closed_ports.remove(port)
        else:
            print("Invalid port number. Please enter a number between 1 and", num_ports)

        attempts -= 1

    if len(open_ports) == 0:
        print("\nCongratulations! You have successfully found all the open ports and gained access to the camera.")
    else:
        print(f"\nGame Over! You found {correct_guesses} out of {len(open_ports) + correct_guesses} open ports.")

port_scanning()