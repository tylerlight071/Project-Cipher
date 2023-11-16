class MarkusSystem:
    def __init__(self):
    self.files = [
        {
            "name": "system_log.txt",
            "content": (
                "System Log for Enigma Corps\n\n"
                "Date: [Timestamp]\n"
                "Event Type: [Event Type]\n"
                "Description: [Description of the event]\n\n"
                "Date: [Timestamp]\n"
                "Event Type: [Event Type]\n"
                "Description: [Description of the event]\n\n"
                "Date: [Timestamp]\n"
                "Event Type: [Event Type]\n"
                "Description: [Description of the event]\n\n"
                "This system log provides a record of important events and activities on Enigma Corps systems for troubleshooting and analysis."
            )
        },
        {
            "name": "technical_documentation.docx",
            "content": (
                "Technical Documentation for Enigma Corps System\n\n"
                "1. System Architecture\n"
                "2. Network Configuration\n"
                "3. Security Protocols\n"
                "4. Troubleshooting Guide\n"
                "5. Software Installation Procedures\n"
                "6. Hardware Specifications\n\n"
                "This documentation provides comprehensive information about the Enigma Corps system for reference and troubleshooting purposes."
            )
        },
        {
            "name": "network_diagram.png",
            "content": "Image file depicting the network architecture of Enigma Corps, detailing server locations, firewalls, and network connections."
        },
        {
            "name": "passwords.txt",
            "content": (
                "Admin Password: *********\n"
                "Database Password: *********\n"
                "Router Password: *********\n"
                "WiFi Password: *********\n"
                "Encryption Key: *********\n\n"
                "Note: Keep this file secure and do not share passwords without proper authorization."
            )
        },
        {
            "name": "software_inventory.csv",
            "content": (
                "Software Inventory for Enigma Corps\n\n"
                "Software Name, Version, License Key\n"
                "1. Enigma Security Suite, v2.0, XXXX-XXXX-XXXX-XXXX\n"
                "2. DataGuard Backup, v1.5, YYYY-YYYY-YYYY-YYYY\n"
                "3. Office Suite, v2022, ZZZZ-ZZZZ-ZZZZ-ZZZZ\n"
                "4. VPN Client, v3.1, WWWW-WWWW-WWWW-WWWW\n"
                "5. Project Management Tool, v4.2, VVVV-VVVV-VVVV-VVVV\n\n"
                "This inventory tracks the software used across Enigma Corps systems."
            )
        }
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
