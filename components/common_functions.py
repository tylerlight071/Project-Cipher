import time

# Makes the text have a delay of (x) when printed to screen
def print_slow(text, delay=0.00):  # change to 0.01
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')