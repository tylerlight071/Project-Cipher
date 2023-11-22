# billy_system.py
from components.common_functions import print_slow


class BillySystem:
    def __init__(self):
        self.files = [
            {
                "name": "cover_letter.txt",
                "content": (
                    "Dear Hiring Manager,\n\n"
                    "I am writing to express my interest in the management position at Enigma Corps. "
                    "I have been with the company for over 7 years and have consistently demonstrated my commitment to driving excellence and fostering collaboration within the team.\n\n"
                    "During my tenure at Enigma Corps, I have been involved in various projects, including the successful completion of the Q3 deliverables project, where I played a key role in the planning and execution stages. "
                    "My dedication to achieving project milestones and my ability to work under pressure make me a strong candidate for a management role.\n\n"
                    "I possess strong leadership skills, which I have honed through my experiences in leading teams and coordinating cross-functional efforts. "
                    "My ability to communicate effectively and build positive relationships with team members and stakeholders has resulted in successful project outcomes and increased productivity.\n\n"
                    "In addition to my technical and leadership skills, I am also committed to continuous learning and professional development. "
                    "I have participated in various training programs and workshops to enhance my management skills and stay up-to-date with industry trends and best practices.\n\n"
                    "I am excited about the opportunity to contribute to the growth and success of Enigma Corps as a member of the management team. "
                    "I am confident that my skills and experience will be valuable assets to the company, and I look forward to the opportunity to work closely with the team to drive innovation and excellence.\n\n"
                    "Thank you for considering my application. I am looking forward to the opportunity to discuss my qualifications further and explore how I can contribute to the success of Enigma Corps.\n\n"
                    "Sincerely,\n"
                    "Billy Constantine\n"
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
                "name": "meeting_minutes.txt",
                "content": (
                    "Meeting Minutes\n\n"
                    "Date: 24/06/2025\n"
                    "Location: REDACTED\n"
                    "Attendees: Amy, REDACTED, Billy, Kyle, REDACTED, REDACTED, REDACTED\n\n"
                    "Agenda:\n"
                    "- Discuss progress on Project REDACTED\n"
                    "- Review safety protocols for handling sensitive materials\n"
                    "- Plan next steps for research and development\n\n"
                    "Action Items:\n"
                    "- Compile data from recent experiments and share with team\n"
                    "- Schedule training session on updated safety protocols\n"
                    "- Develop timeline for next phase of Project X\n\n"
                    "Next Meeting: 05/08/24, 12:00pm\n"
                )
            },
            {
                "name": "employee_performance_review.txt",
                "content": (
                    "Employee Performance Review\n\n"
                    "Employee Name: Billy Constantine\n"
                    "Employee ID: 035854\n"
                    "Review Date: 28/06/2024\n\n"
                    "Performance Summary:\n"
                    "Billy has demonstrated exceptional performance in his role as a sales representative. He has consistently exceeded sales targets, built strong relationships with clients, and demonstrated leadership qualities in team meetings and projects.\n\n"
                    "Strengths:\n"
                    "- Exceeded quarterly sales targets by 15%.\n"
                    "- Successfully onboarded and mentored two new team members.\n"
                    "- Demonstrated excellent communication and negotiation skills.\n\n"
                    "Areas for Improvement:\n"
                    "- Time management skills can be further developed to ensure all tasks are completed in a timely manner.\n"
                    "- Continued development of technical knowledge to stay up-to-date with industry trends.\n"
                    "- Strengthen collaboration with cross-functional teams to drive more integrated solutions.\n\n"
                    "Goals for Next Review Period:\n"
                    "- Increase sales targets by 20%.\n"
                    "- Complete a management training program.\n"
                    "- Improve time management skills through prioritization and delegation.\n\n"
                    "Overall Rating: 4.5/5\n"
                    "Reviewer Name: Katie Thompson\n"
                    "Reviewer Signature: Katie Thompson\n"
                    "Date: 28/06/2024\n"
                )
            }
        ]
        self.emails = [

            {
                "sender": "Billy",
                "subject": "Re: Need Your Help on the Smith Project",
                "body": (
                    "Hi Amy,\n\n"
                    "I hope this message finds you in great spirits! I'm more than happy to lend a helping hand with the Smith project. After all, two heads are better than one, especially when it comes to data analysis, right?\n\n"
                    "How about we grab a coffee and chat about the project in person? I think it would be nice to catch up and discuss the data over a cup of joe. I'm sure we can brainstorm some ideas and come up with a game plan together.\n\n"
                    "I'm free [date] at [time], does that work for you? If not, just let me know your availability, and we can find a time that suits us both. I'm really looking forward to our coffee date and tackling the project together.\n\n"
                    "Can't wait to see you and dive into the data!\n\n"
                    "Best,\n"
                    "Billy"
                )
            },
            {
                "sender": "Billy",
                "subject": "Project Update",
                "body": (
                    "Hello Team,\n\n"
                    "I wanted to provide everyone with a quick update on our progress with the Q3 deliverables project. We've successfully completed the initial research phase and are now moving into the planning stage.\n\n"
                    "In our last meeting, we discussed the following key points:\n"
                    "- Compound Analysis: We've identified a unique compound with potential applications in various industries. Further testing and analysis are required to unlock its full potential.\n"
                    "- Resource Management: We've allocated a special team and dedicated resources to handle the delicate nature of this project, ensuring utmost confidentiality and security.\n"
                    "- Safety Protocols: We've developed strict safety protocols to handle the compound, and we're conducting regular training sessions to ensure compliance.\n\n"
                    "Our next steps include finalizing the project plan, assigning tasks to team members, and setting deadlines. I would appreciate input and feedback from all team members to ensure we're on the right track. Please review the attached project plan document for more details.\n\n"
                    "Additionally, I want to remind everyone of the confidential nature of this project. It's imperative that we maintain discretion and follow all security protocols to safeguard our work. Let's work together to make this project a success and uphold the company's reputation for innovation and excellence.\n\n"
                    "If you have any questions or concerns, please don't hesitate to reach out. Your cooperation and commitment to this project are greatly appreciated.\n\n"
                    "Best regards,\n"
                    "Billy"
                )
            },
            {
                "sender": "Billy",
                "subject": "Re: Can't Stop Thinking About You",
                "body": (
                    "Hey there, Amy,\n\n"
                    "Wow, your message really caught me by surprise! But in the best way possible, of course. I've been trying to play it cool, but I have to admit, I've been thinking about that night a lot too. There was just something electric in the air, wasn't there?\n\n"
                    "I've been tossing and turning, wondering if I should reach out to you or if I should wait for you to make the first move. I guess you beat me to it, and I'm glad you did. It's like you read my mind.\n\n"
                    "I can't deny that there's a certain chemistry between us, and I'm intrigued to see where it could lead. I agree that our lives are complicated, and we don't want to add more stress to each other's plates. But sometimes, taking a risk is what makes life exciting, don't you think?\n\n"
                    "I don't want to rush things or make you feel pressured in any way. I'm more than happy to take things slow and let them unfold naturally. But I can't help but imagine the possibilities if we give this a real shot. We could have something truly special, and I don't want to let that pass us by.\n\n"
                    "How about we meet up for dinner and drinks next week? We can talk about it more and see where the night takes us. I think it would be a fun and relaxed way to get to know each other better and explore this connection we have. What do you say?\n\n"
                    "I hope you're doing well, and I'm eagerly awaiting your reply. Until then, I'll be daydreaming about our next encounter.\n\n"
                    "Take care, and talk to you soon.\n\n"
                    "Yours truly,\n"
                    "Billy"
                )
            },
            {
                "sender": "Billy",
                "subject": "Re: Thank You for Letting Me Use Your Computer",
                "body": (
                    "Hey Amy,\n\n"
                    "No problem at all! I'm always here to help out when I can. It's what teammates do, right?\n\n"
                    "Oh, and about the password thing – haha, I know it's not the most secure choice. I've been meaning to change it, but I guess old habits die hard, right? "
                    "Thanks for looking out for me though! I'll try to come up with something a bit more creative next time.\n\n"
                    "If you ever need anything else, just give me a shout. Happy to help!\n\n"
                    "Take care,\n"
                    "Billy"
                )
            },
            {
                "sender": "Billy",
                "subject": "Professional Development",
                "body": (
                    "Good Evening Katie,\n\n"
                    "I hope this email finds you well. I'm reaching out to express my interest in professional development opportunities within the company, particularly in the area of management and leadership.\n\n"
                    "I've been with the company for several years now, and I've had the chance to work on various projects and collaborate with different teams. I'm keen to build on this experience and take on more responsibility, and I believe that acquiring the necessary skills for a management role would be a great next step in my career.\n\n"
                    "Could you please provide information on available training programs, workshops, or seminars that focus on leadership development and management skills? I'm particularly interested in areas such as team leadership, strategic planning, conflict resolution, and decision-making.\n\n"
                    "Additionally, if there are any tuition reimbursement programs or resources for management training and certification, I'd like to learn more about them. I'm committed to investing time and effort in my professional growth and believe that these opportunities would greatly benefit both myself and the company.\n\n"
                    "Your guidance and assistance in exploring these options would be greatly appreciated. I look forward to your response and any recommendations you may have.\n\n"
                    "Thank you for your support, and I'm excited about the prospect of contributing to the company's success in a management role.\n\n"
                    "Best regards,\n"
                    "Billy"
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


