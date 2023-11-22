from components.common_functions import print_slow


class MarkusSystem:
    def __init__(self):
        self.files = [
            {
                "name": "system_log.txt",
                "content": (
                    "Enigma Corps System Log\n\n"
                    "Date: 2023-11-16 08:00 AM\n"
                    "Event Type: System Startup\n"
                    "Description: The Enigma Corps systems smoothly initiated startup procedures, ensuring a seamless beginning to the workday.\n\n"
                    "Date: 2023-11-16 10:30 AM\n"
                    "Event Type: Network Upgrade\n"
                    "Description: Implemented a network upgrade to enhance data transfer speeds, providing improved efficiency across departments.\n\n"
                    "Date: 2023-11-16 01:45 PM\n"
                    "Event Type: Security Patch Applied\n"
                    "Description: Critical security patch successfully applied to safeguard against potential vulnerabilities, ensuring system integrity.\n\n"
                    "Date: 2023-11-16 04:20 PM\n"
                    "Event Type: Server Maintenance\n"
                    "Description: Conducted routine maintenance on Enigma Corps servers, optimizing performance and minimizing downtime.\n\n"
                    "This dynamic system log captures key events, from the smooth startup of the day to network upgrades, security enhancements, and routine maintenance. It serves as a valuable record for troubleshooting and analysis, ensuring the optimal functionality of Enigma Corps systems."
                )
            },
            {
                "name": "technical_documentation.docx",
                "content": (
                    "Enigma Corps System Technical Documentation\n\n"
                    "1. System Architecture:\n"
                    "   - Overview of the system's structural design and components.\n\n"
                    "2. Network Configuration:\n"
                    "   - Details on the configuration of Enigma Corps' network setup for efficient communication.\n\n"
                    "3. Security Protocols:\n"
                    "   - Comprehensive overview of security measures and protocols implemented to safeguard sensitive data.\n\n"
                    "4. Troubleshooting Guide:\n"
                    "   - Step-by-step guide for identifying and resolving common issues to ensure seamless system functionality.\n\n"
                    "5. Software Installation Procedures:\n"
                    "   - Instructions for installing and updating software components within the Enigma Corps system.\n\n"
                    "6. Hardware Specifications:\n"
                    "   - Detailed specifications of the hardware components utilized in the Enigma Corps infrastructure.\n\n"
                    "This meticulously crafted technical documentation serves as a go-to resource for understanding the Enigma Corps system, covering everything from its architecture and network configuration to security protocols, troubleshooting, and hardware specifications. It's an invaluable reference for maintaining optimal system performance."
                )
            },
            {
                "name": "passwords.txt",
                "content": (
                    "Sensitive Password Information for Enigma Corps\n\n"
                    "Admin Password: *********\n"
                    "Database Password: *********\n"
                    "Router Password: *********\n"
                    "WiFi Password: *********\n"
                    "Encryption Key: *********\n\n"
                    "Warning: This file contains confidential information. Keep it secure, and refrain from sharing passwords without explicit authorization. Safeguarding this information is crucial to maintaining the security and integrity of the Enigma Corps systems."
                )
            },
            {
                "name": "software_inventory.csv",
                "content": (
                    "Software Inventory for Enigma Corps\n\n"
                    "Software Name, Version, License Key\n"
                    "1. Enigma Security Suite, v2.0, X1Y2Z3A4-B5C6D7E8-F9G0H1I2\n"
                    "2. DataGuard Backup, v1.5, Y3X2W1V0-U9T8S7R6-Q5P4O3N2\n"
                    "3. Office Suite, v2022, Z9Z8Z7Z6-Z5Z4Z3Z2-Z1Z0Z9Z8-Z7Z6Z5\n"
                    "4. VPN Client, v3.1, W6W5W4W3-W2W1W0-W9W8W7-W6W5W4\n"
                    "5. Project Management Tool, v4.2, VV8V7V6V5-V4V3V2V1-V0V9V8V7-V6V5V4\n\n"
                    "Important: This inventory is crucial for tracking and managing software across Enigma Corps systems. The provided license keys are randomized for security reasons. Handle this information responsibly, and ensure it is only accessible to authorized personnel to maintain the security and compliance of our software assets."
                )
            }
        ]
        self.emails = [
            # Email to Management
            {
                "sender": "Markus",
                "subject": "System Maintenance Scheduled",
                "body": (
                    "Dear Michael,\n\n"
                    "I hope this email finds you well. We wanted to inform you that we have scheduled a system maintenance session for the upcoming weekend to ensure the optimal performance and security of our systems.\n\n"
                    "Maintenance Details:\n"
                    "- Date: 16/12/23 - 17/12/23\n"
                    "- Time: 3:00pm\n"
                    "- Duration: 1 Hour\n"
                    "- Impact: No impact expected\n\n"
                    "During this period, there might be temporary disruptions in certain services. Our team will be working diligently to minimize any inconvenience. If you have any concerns or specific considerations, please feel free to reach out to us.\n\n"
                    "Thank you for your understanding and cooperation.\n\n"
                    "Best regards,\n"
                    "IT Department"
                )
            },
            {
                # Email to Employees
                "sender": "Markus",
                "subject": "Upcoming Software Update",
                "body": (
                    "Good afternoon, Kyle,\n\n"
                    "We hope you're doing well. Our IT team is excited to inform you about an upcoming software update that will enhance the functionality and security of our systems. The update is scheduled for [Date] at [Time]. Please take note of the following details:\n\n"
                    "- Expected Duration: Two Days\n"
                    "- Action Required: As this will be processed during the weekend, no action is required.\n"
                    "- Impact: While we anticipate minimal impact on your day-to-day activities, it's essential to be aware of any potential changes. These include: New UI to navigate, logging in or logging out issues.\n\n"
                    "We recommend saving your work and logging out of your system before the update. If you encounter any issues post-update, don't hesitate to contact our IT support team for assistance.\n\n"
                    "Thank you for your cooperation and understanding.\n\n"
                    "Best regards,\n"
                    "IT Support Team"
                )
            },
            # Email from Markus to Billy
            {
                "sender": "Markus",
                "subject": "Urgent: Password Security Update Required",
                "body": (
                    "Billy,\n\n"
                    "I hope this email finds you well. I wanted to bring to your attention the importance of updating your current password. This is not the first time I've raised this concern, and I want to emphasize its critical nature.\n\n"
                    "In recent security assessments, it has been flagged that your current password might not meet the latest security standards. To ensure the safety of your account and our overall cybersecurity, it is imperative that you change your password promptly.\n\n"
                    "I understand that these reminders may seem repetitive, but they stem from a genuine concern for the security of your account and our collective responsibility in maintaining a robust cybersecurity posture.\n\n"
                    "Please take a moment at your earliest convenience to update your password. If you encounter any issues or have questions, feel free to reach out. Your cooperation is greatly appreciated.\n\n"
                    "Best regards,\n"
                    "Markus, Security Team"
                )
            }

        ]

    def list_files(self):
        print_slow("\nFiles:")
        for file in self.files:
            print_slow(f"\n{file['name']}")

    def read_file(self, file_name):
        file_found = False
        for file in self.files:
            if file['name'] == file_name:
                file_found = True
                return file['content']

        if not file_found:
            print_slow("\nNo file found with that name, please try again.")
            return None

    def list_emails(self):
        print_slow("\nEmails:")
        for i, email in enumerate(self.emails):
            print_slow(f"\n{email['subject']} - From: {email['sender']}")

    def read_email(self, subject):
        for email in self.emails:
            if email['subject'].lower() == subject.lower():
                print_slow(f"\nFrom: {email['sender']}\nSubject: {email['subject']}\n\n{email['body']}")
                return
        print_slow("\nNo email found with that subject, please try again.")
