# amy_system.py

class AmySystem:
    def __init__(self):
        self.files = [
            {
                "name": "return_to_work_form.txt",
                "content": (
                    "Employee Name: _______________\n"
                    "Employee ID: ____________\n"
                    "Department: _______________\n"
                    "Date of Return: ______\n\n"
                    "I, [Employee Name], certify that I have followed the company's "
                    "guidelines for returning to work after an absence. "
                    "I understand that it is my responsibility to adhere to all safety "
                    "protocols and procedures to ensure the health and well-being of my "
                    "colleagues and myself.\n\n"
                    "I acknowledge that I have completed any necessary training and have "
                    "been briefed on any updates to the company's policies and procedures. "
                    "I am aware that I must report any symptoms or exposure to COVID-19 to "
                    "my supervisor immediately.\n\n"
                    "I am committed to doing my part to maintain a safe and healthy work "
                    "environment for everyone. I will continue to follow all guidelines "
                    "and protocols and will cooperate with any additional measures that "
                    "may be implemented in the future.\n\n"
                    "Signature: [Employee Signature]\n"
                    "Date: [Date]"
                )
            },
            {
                "name": "employee_handbook.txt",
                "content": (
                    "Welcome to Enigma Corps We are thrilled to have you as part of our "
                    "team. This employee handbook has been designed to help you understand "
                    "our company's policies, procedures, and expectations.\n\n"
                    "Our company is committed to fostering a positive and inclusive work "
                    "environment where all employees feel valued and supported. We believe "
                    "in treating everyone with respect and dignity and expect all employees "
                    "to do the same.\n\n"
                    "In this handbook, you will find information on topics such as:\n\n"
                    "- Code of Conduct\n"
                    "- Dress Code\n"
                    "- Attendance and Punctuality\n"
                    "- Time Off and Leave Policies\n"
                    "- Performance Evaluations\n"
                    "- Health and Safety\n"
                    "- Equal Employment Opportunity\n"
                    "- Harassment and Discrimination\n\n"
                    "Please take the time to read through this handbook carefully and "
                    "familiarize yourself with our policies and procedures. If you have any "
                    "questions or concerns, do not hesitate to reach out to your supervisor "
                    "or the HR department.\n\n"
                    "We look forward to working with you and hope you have a long and "
                    "successful career with Enigma Corps!"
                )
            },
            {
                "name": "benefits_summary.txt",
                "content": (
                    "At Enigma Corps, we believe in taking care of our employees and "
                    "offer a comprehensive benefits package to support your health, well-being, "
                    "and financial security. Below is a summary of the benefits available to "
                    "you as an employee of Enigma Corps.\n\n"
                    "Health Insurance: We offer a choice of medical, dental, and vision "
                    "plans to meet your needs. Our plans provide coverage for preventive care, "
                    "hospitalization, prescription drugs, and more.\n\n"
                    "Retirement Savings: We offer a 401(k) plan with a generous company "
                    "match to help you save for your future. You can choose from a variety of "
                    "investment options to suit your needs.\n\n"
                    "Paid Time Off: We provide a generous amount of paid time off, "
                    "including vacation, sick leave, and holiday pay. We also offer paid "
                    "parental leave for new parents.\n\n"
                    "Flexible Work Arrangements: We understand the importance of work-life "
                    "balance and offer flexible work arrangements, such as remote work and "
                    "flexible schedules, where possible.\n\n"
                    "Wellness Programs: We offer a variety of wellness programs and "
                    "resources to support your physical and mental health, including fitness "
                    "classes, stress management programs, and counseling services.\n\n"
                    "Professional Development: We are committed to supporting your growth "
                    "and development and offer a variety of training and development "
                    "opportunities, including tuition reimbursement, workshops, and seminars."
                    "\n\n"
                    "We encourage you to review this summary carefully and take advantage of "
                    "the benefits available to you. If you have any questions or need further "
                    "information, please contact the HR department."
                )
            },
        ]
        self.emails = [
            {
                "sender": "Amy",
                "subject": "Can't Stop Thinking About You",
                "body": (
                    "Hey Billy,\n\n"
                    "I hope this message finds you in good spirits. I've been meaning to write to you for a while now, but I couldn't find the right words to express what I've been feeling.\n\n"
                    "Ever since that night we spent together, I can't seem to get you out of my mind. There's something about the way you make me feel that I've never experienced before. "
                    "It's exhilarating, yet terrifying all at the same time.\n\n"
                    "I know we both have a lot on our plates right now, and I don't want to add any more stress to your life. But I can't help but wonder what could happen if we gave this a real shot. "
                    "I know it's complicated, and there are a lot of factors to consider, but I think we owe it to ourselves to explore this connection we have.\n\n"
                    "I understand if you're not ready to take that step, and I don't want to pressure you into anything you're not comfortable with. "
                    "But I can't shake the feeling that we could have something truly special together.\n\n"
                    "I'd love to hear your thoughts on this, and I'm more than willing to take things slow if that's what you need. Maybe we could meet up for dinner and talk about it in person?"
                    " I think it would be easier to have this conversation face-to-face.\n\n"
                    "I hope you're doing well, and I look forward to hearing from you soon.\n\n"
                    "Take care,\n"
                    "Amy"
                )
            },
            {
                "sender": "Amy",
                "subject": "Need Your Help on the Smith Project",
                "body": (
                    "Hi Billy,\n\n"
                    "I hope this email finds you well. I wanted to reach out and ask for your help on the Smith project. I've been having some trouble with the data analysis portion, and I know you have a lot of experience in that area.\n\n"
                    "The project involves analyzing customer feedback data to identify trends and areas for improvement. I've been working on it for a few weeks now, but I'm finding it challenging to make sense of the data and draw meaningful conclusions.\n\n"
                    "Would you be available for a quick meeting later this week to go over some of the data with me? I would really appreciate your input and guidance on this. I think your expertise could really help me make progress and ensure the success of the project.\n\n"
                    "If you're available, please let me know your preferred date and time, and I'll send out a calendar invite. I'm flexible and can work around your schedule.\n\n"
                    "Thank you in advance for your help, and I look forward to hearing from you soon.\n\n"
                    "Best,\n"
                    "Amy"
                )
            },
            {
                "sender": "Amy",
                "subject": "Request for Time Off",
                "body": (
                    "Hi Kyle,\n\n"
                    "I hope this email finds you well. I wanted to request some time off next month for a family vacation. I am planning to be out of the office from [start date] to [end date].\n\n"
                    "I have been working hard on the Johnson project and have made significant progress. I will make sure to finish up any outstanding work and hand off any ongoing projects to my colleagues before I leave. I will also be available by email in case of any urgent matters.\n\n"
                    "I understand that this is a busy time for the team, and I want to ensure that my absence doesn't cause any disruptions. I have already spoken to [Colleague's Name] and [Colleague's Name], and they have kindly agreed to cover for me while I'm away.\n\n"
                    "Thank you for considering my request. I look forward to spending some quality time with my family and coming back to work refreshed and recharged. I am confident that the time off will help me come back with renewed energy and focus.\n\n"
                    "Best,\n"
                    "Amy"
                )
            },
            {
                "sender": "Amy",
                "subject": "Apology for the Mistake",
                "body": (
                    "Hi Katie,\n\n"
                    "I hope this email finds you well. I wanted to reach out and apologize for the mistake I made on the Johnson report. I realize now that I overlooked some important data, and I take full responsibility for it.\n\n"
                    "I have gone back and corrected the report, and I will make sure to double-check my work in the future to avoid any similar mistakes. I have also attached the updated report for your reference.\n\n"
                    "I understand if you are disappointed or frustrated, and I am more than willing to do whatever it takes to make it right. Please let me know if there's anything else I can do to fix this,"
                    "\nor if you would like to discuss this further.\n\n"
                    "Once again, I am truly sorry for the mistake, and I appreciate your understanding. I value our working relationship and hope that this incident doesn't tarnish it. I am committed to making amends and ensuring that this doesn't happen again in the future.\n\n"
                    "Best,\n"
                    "Amy"
                )
            }
        ]

    def list_files(self):
        print("\nFiles:")
        for file in self.files:
            print(f"\n{file['name']}")

    def read_file(self, file_name):
        for file in self.files:
            if file['name'] == file_name:
                print(f"\nReading {file_name}...\n\n{file['name']}:\n{file['content']}")
                return
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
