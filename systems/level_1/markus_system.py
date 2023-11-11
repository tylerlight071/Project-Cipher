class MarkusSystem:
    def __init__(self):
        self.files = [
        
        ]
        self.emails = [
            
        ]

    def list_files(self):
        print("\nFiles:")
        for file in self.files:
            print(f"\n{file['name']}")

    def read_file(self, file_name):
        file_found = False
        for file in self.files:
            if file['name'] == file_name:
                file_found = True
                return file['content']

        if not file_found:
            print("\nNo file found with that name, please try again.")
            return None

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
