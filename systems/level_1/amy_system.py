#amy_system.py

class AmySystem:
    def __init__(self):
        self.files = ["file1.txt", "file2.txt", "file3.txt"]
        self.emails = [
            {
                "sender": "Amy",
                "subject": "Help me!",
                "body": (
                    "Cipher, I need your help. I've discovered something that could change everything. "
                    "I've hidden a file in my system that contains vital information about Enigma Corp's secrets. "
                    "\nI need you to hack into my system and retrieve the file. The password to my system is 'sexinthecity'. "
                    "Please hurry, I don't know how much longer I can keep this a secret."
                )
            }
        ]

    def list_files(self):
        print("\nFiles:")
        for file in self.files:
            print(file)

    def read_file(self, file_name):
        if file_name in self.files:
            print(f"\nReading {file_name}...")
            # TODO: Implement file reading logic
        else:
            print("\nFile not found! Please try again.")

    def list_emails(self):
        print("\nEmails:")
        for i, email in enumerate(self.emails):
            print(f"\n{email['subject']} - From: {email['sender']}")

    def read_email(self, subject):
        for email in self.emails:
            if email['subject'].lower() == subject.lower():
                print(f"\nFrom: {email['sender']}\nSubject: {email['subject']}\n\n{email['body']}")
                return
        print("\nNo email found with that subject, please try again.")
