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
            read_email(emails, subject, triggered_emails)
        elif command.lower() == 'help':
            # Display mail help message
            mail_help()
        elif command.lower() == 'exit':
            # Exit mail system
            print_slow(Fore.LIGHTBLUE_EX + "\nExiting Mail System..." + Style.RESET_ALL)
            break
        else:
            print_slow(Fore.RED + "\nInvalid command, please try again." + Style.RESET_ALL)