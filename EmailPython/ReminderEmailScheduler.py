# Import necessary libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from typing import List, Dict, Optional
from datetime import datetime
import smtplib
import os
import time
import schedule
import re
import spacy 

# Load environment variables from .env file
load_dotenv()

# Fetch credentials from environment variables
password = os.getenv('MAIL_PASSWORD')
username = os.getenv('MAIL_USERNAME')
mail_username = os.getenv('MAIL_USERNAME')

# Load English NLP model from spaCy
try: 
    nlp = spacy.load("en_core_web_sm")
except OSError:
    raise OSError("Error loading spaCy model.")

# EmailScheduler class to handle email scheduling and sending
class EmailScheduler:
    # Initialize the EmailScheduler with sender credentials
    def __init__(self):
        self.sender_email = os.getenv('MAIL_USERNAME')
        self.sender_password = os.getenv('MAIL_PASSWORD')

        if not self.sender_email or not self.sender_password:
            raise ValueError("Email credentials are not set in the environment variables.")
        
        self.schedule_jobs = []
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
    
    # Function to parse the email command and extract details
    def parse_email_command(self, command: str) -> Dict:
        doc = nlp(command)

        # Initialize variables to store parsed information
        email_details = {
            "subject": '',
            "recipient": '',
            "body": '',
            "schedule": {}
        }

        # Extract recipent 
        for i, token in enumerate(doc):
            if token.text.lower() == "to" and i + 1 < len(doc):
                # Look ahed to capture the full email address if it exists
                recipient = doc[i + 1].text
                # 
                j = i + 2
                while j < len(doc) and (doc[j].text == "@" or "." in doc[j].text):
                    recipient += " " + doc[j].text
                    j += 1
                email_details["recipient"] = recipient.strip()
                break
        
        # Extract subject
        for i, token in enumerate(doc):
            if token.text.lower() == 'to':
                email_details['subject'] = ' '.join([t.text for t in doc[:i]])
                break

        # Extract schedule information
        time_pattern = re.compile(r'at\s+(\d{1,2})(?::(\d{2}))?\s*([ap]m)?', re.IGNORECASE)
        time_match = time_pattern.search(command)
        
        day_pattern = re.compile(r'(every|each)\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)', re.IGNORECASE)
        day_match = day_pattern.search(command)
        
        date_pattern = re.compile(r'on\s+(\w+\s+\d{1,2}(?:\s*,\s*\d{4})?)', re.IGNORECASE)
        date_match = date_pattern.search(command)
        
        if time_match:
            hour = int(time_match.group(1))
            minute = int(time_match.group(2)) if time_match.group(2) else 0
            period = time_match.group(3).lower() if time_match.group(3) else ''
            
            # Convert to 24-hour format
            if period == 'pm' and hour != 12:
                hour += 12
            elif period == 'am' and hour == 12:
                hour = 0
                
            email_details['schedule']['time'] = f"{hour:02d}:{minute:02d}"
            
        if day_match:
            email_details['schedule']['day'] = day_match.group(2).lower()
            
        if date_match:
            email_details['schedule']['date'] = date_match.group(1)
            try:
                # Try to parse the date string
                parsed_date = datetime.strptime(email_details['schedule']['date'], '%B %d, %Y')
                email_details['schedule']['date_obj'] = parsed_date
            except ValueError:
                try:
                    parsed_date = datetime.strptime(email_details['schedule']['date'], '%b %d, %Y')
                    email_details['schedule']['date_obj'] = parsed_date
                except ValueError:
                    try:
                        parsed_date = datetime.strptime(email_details['schedule']['date'], '%m/%d/%Y')
                        email_details['schedule']['date_obj'] = parsed_date
                    except ValueError:
                        print(f"Warning: Could not parse date {email_details['schedule']['date']}")
                        del email_details['schedule']['date']
            
        # Default body (can be enhanced with more sophisticated parsing)
        email_details['body'] = f"Reminder: {email_details['subject']}"
            
        return email_details
    
    # Function to send an email with a custom signature
    def send_email(self, recipient: str, subject: str, body: str) -> None:
        # Custom signature to append at the end of each email
        signature = """
        <br><br>
        <div style="font-family: 'Trebuchet MS', sans-serif; color: #003366; font-size: 10pt;">
            <span style="font-weight: normal;">Best regards,</span><br>
            <span style="font-size: 14pt; font-weight: bold; font-style: italic;">David Caleb Chaparro Orozco</span><br>
            <span style="font-weight: bold; color: white;">Software Engineer | Data Scientist | Data Engineer | Python Developer | AI & ML Specialist | Big Data | Analytics</span><br>
            <span style="font-weight: bold; color: white;">Medellín, Colombia</span><br>
            <span style="font-weight: bold; color: white;">+57 314 650 8234</span><br>
            <span style="font-weight: bold; font-style: italic;">davidcaleb1998@gmail.com</span><br>
            <span style="font-weight: bold; font-style: italic;">
                <a href="https://www.linkedin.com/in/caleb1998/" style="color: #003366; text-decoration: none;">LinkedIn</a> |
                <a href="https://github.com/DavidCalebChaparroOrozco/Daily-Projects/" style="color: #003366; text-decoration: none;">Portfolio</a>
            </span>
        </div>
        """
        try: 
            # Create the email message
            msg = MIMEMultipart("alternative")
            msg["From"] = self.sender_email
            msg["To"] = recipient
            msg["Subject"] = subject

            # Add the body to the email
            html_body = f"{body}{signature}"
            part = MIMEText(html_body, "html")
            msg.attach(part)

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                # Upgrade to secure connection
                server.starttls()  
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)

            print(f"Email sent to {recipient} with subject: {subject}")
        except Exception as e:
            print(f"Failed to send email to {recipient}. Error: {e}")

    # Function to schedule an email based on parsed details
    def schedule_email(self, recipient: str, subject: str, body: str, schedule_info: Dict) -> None:
        if 'time' in schedule_info and 'day' in schedule_info:
            # Weekly schedule
            time_str = schedule_info['time']
            day_of_week = schedule_info['day'].capitalize()

            # Map day names to schedule's day names
            day_map = {
                'Monday': schedule.every().monday,
                'Tuesday': schedule.every().tuesday,
                'Wednesday': schedule.every().wednesday,
                'Thursday': schedule.every().thursday,
                'Friday': schedule.every().friday,
            }

            if day_of_week in day_map:
                job = day_map[day_of_week].at(time_str).do(
                    self.send_email,
                    recipient=recipient,
                    subject=subject,
                    body=body
                )
                self.schedule_jobs.append((job, f"Every {day_of_week.capitalize()} at {time_str}"))
                print(f"Email scheduled every {day_of_week.capitalize()} at {time_str} to {recipient}")
            else:
                print(f"Invalid day specified: {day_of_week}. Please use a valid day of the week.")
        
        elif 'time' in schedule_info and 'date_obj' in schedule_info:
            # One-time schedule on specific date and time
            schedule_time = schedule_info['date_obj']
            now = datetime.now()

            if schedule_time < now:
                print("Cannot schedule an email in the past.")
                return
            
            delay = (schedule_time - now).total_seconds()

            # Schedule a one-time job
            def send_and_remove_job():
                self.send_email(recipient, subject, body)
                # Remove the job after sending
                for i, (job, desc) in enumerate(self.schedule_jobs):
                    if desc.startswith("One-time on"):
                        self.schedule_jobs.pop(i)
                        break
            
            job = schedule.every().day.at("00:00").do((send_and_remove_job).tag("one-time"))
            self.schedule_jobs.append((job, f"One-time on {schedule_time.strftime('%Y-%m-%d %H:%M:%S')}"))
            print(f"Email scheduled for one-time on {schedule_time.strftime('%Y-%m-%d %H:%M:%S')} to {recipient}")

        elif 'time' in schedule_info:
            # Daily schedule at specific time
            time_str = schedule_info['time']
            job = schedule.every().day.at(time_str).do(
                self.send_email,
                recipient=recipient,
                subject=subject,
                body=body
            )
            self.schedule_jobs.append((job, f"Daily at {time_str}"))
            print(f"Email scheduled daily at {time_str} to {recipient}")
        else:
            print("No valid schedule information provided. Email not scheduled.")
    # Function to list all scheduled emails
    def list_scheduled_emails(self) -> None:
        if not self.schedule_jobs:
            print("No emails currently scheduled.")
            return
        
        print("\nCurrently scheduled emails:")
        for i, (job, desc) in enumerate(self.schedule_jobs, 1):
            print(f"{i}. {desc}")

    # Function to run the scheduler in a loop
    def run_scheduler(self) -> None:
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Function to clear all scheduled emails
    def clear_scheduled_emails(self) -> None:
        schedule.clear()
        self.schedule_jobs.clear()
        print("All scheduled emails have been cleared.")

# Function to send a test email
def send_test_email():
    try:
        scheduler = EmailScheduler()
        subject = "🚀 Test Email from David Caleb"
        body = "This is a test email sent from your Python Email Scheduler."
        # Replace with your actual recipient email for testing
        recipient = mail_username
        scheduler.send_email(recipient, subject, body)
    except Exception as e:
        print(f"Error sending test email: {e}")

# EmailCLI class to handle user interaction and scheduling
class EmailCLI:
    # Initialize the EmailCLI and set up the EmailScheduler
    def __init__(self):
        try:
            self.scheduler = EmailScheduler()
        except ValueError as e:
            print(f"Error: {str(e)}")
            print("Please check your email credentials in the .env file.")
            self.scheduler = None
    # Function to display the main menu
    def display_menu(self):
        print("Welcome to the Email Scheduler by David Caleb!")
        print("\nMenu:")
        print("1. Schedule an email")
        print("2. List scheduled emails")
        print("3. Clear all scheduled emails")
        print("4. Run the scheduler")
        print("5. Exit")
    
    # Function to run the main menu loop
    def run_main_menu(self):
        if not self.scheduler:
            return

        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-5): ").strip())
            except ValueError:
                print("Invalid input. Please enter a number from 1 to 5.")
                continue

            if choice == 1:
                self.schedule_email()
            elif choice == 2:
                self.scheduler.list_scheduled_emails()
            elif choice == 3:
                self.scheduler.clear_scheduled_emails()
            elif choice == 4:
                print("Scheduler running in background. Press Ctrl+C to exit.")
                try:
                    self.scheduler.run_scheduler()
                except KeyboardInterrupt:
                    print("\nScheduler interrupted.")
                finally:
                    self.scheduler.clear_scheduled_emails()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Please select a valid option.")

    # Function to handle scheduling an email based on user input
    def schedule_email(self):
        print("\nExample commands:")
        print("- 'Send report to john@example.com every Monday at 8am'")
        print("- 'Remind team about meeting to team@company.com on June 25, 2023 at 2pm'")
        print("- 'Daily status update to manager@work.com at 5pm'\n")

        command = input("Enter your email command: ").strip()
        if not command:
            print("No command entered.")
            return

        try:
            email_details = self.scheduler.parse_email_command(command)
        except Exception as e:
            print(f"Failed to parse email command: {e}")
            return

        print("\nParsed details:")
        print(f"Subject: {email_details['subject']}")
        print(f"Recipient: {email_details['recipient']}")
        print(f"Body: {email_details['body']}")
        print(f"Schedule: {email_details['schedule']}")

        confirm = input("Schedule this email? (y/n): ").lower()
        if confirm == 'y':
            if '@' not in email_details['recipient'] or '.' not in email_details['recipient']:
                print("Warning: The recipient doesn't look like a valid email address.")
                return
            self.scheduler.schedule_email(
                email_details['recipient'],
                email_details['subject'],
                email_details['body'],
                email_details['schedule']
            )
            print("Email scheduled successfully.")
        else:
            print("Email scheduling canceled.")

if __name__ == "__main__":
    # Unique test email to verify functionality
    send_test_email()

    # cli = EmailCLI()
    # cli.run_main_menu()

# Quote:
# Remember what Kobe once said: 
# "I don't relate to lazy people. We don't speak the same language. I don't understand you. I don't want to understand you."