# Importing required libraries
import os
import smtplib
import re
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

# Fetch credentials from environment variables
password = os.getenv('MAIL_PASSWORD')
username = os.getenv('MAIL_USERNAME')

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


# Function to send an email with the project description
def send_mail(subject, body, recipient_email):
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = recipient_email
    msg["From"] = username
    msg["Subject"] = subject

    # Append the signature at the end of the body
    body_with_signature = f"{body}{signature}"
    msg.attach(MIMEText(body_with_signature, "html"))

    s.send_message(msg)
    del msg
    s.quit()

# Function to extract project description by day from README.md
def get_project_by_day(day_number):
    # Match until next "* Day" or EOF
    day_pattern = rf"\* Day {day_number:02d}:(.*?)(?=\n\* Day \d{{2,4}}:|\Z)"  

    # Read the README.md file

    # Get current directory 
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to reach 'DailyProject'
    project_root = os.path.abspath(os.path.join(current_dir, os.pardir))

    # Path to README.md in the parent folder
    readme_path = os.path.join(project_root, "README.md")
    with open(readme_path, "r", encoding="utf-8") as file:
        content = file.read()

        match = re.search(day_pattern, content, re.DOTALL)
        if match:
            raw_text = match.group(1).strip()

            # Remove bold markers '**'
            cleaned_text = re.sub(r"\*\*(.*?)\*\*", r"\1", raw_text)

            # Replace new lines with HTML <br> tags
            formatted_text = cleaned_text.replace('\n', '<br>')

            return f"<h2>Day {day_number:02d}</h2><p>{formatted_text}</p>"
        else:
            return None

# Main program
if __name__ == "__main__":
    try:
        # Ask the user for the day number and recipient email
        day_input = input("Enter the project day number (e.g., 1 for Day 01): ")
        recipient_email = input("Enter the recipient email address: ")

        # Validate the input
        if not day_input.isdigit():
            print("Please enter a valid number.")
            exit()

        day_number = int(day_input)
        if day_number < 1 or day_number > 1000:
            print("Please enter a number between 1 and 1000.")
            exit()

        # Get the project description
        project_description = get_project_by_day(day_number)

        if project_description:
            send_mail(f"Day {day_number:02d} Project", project_description, recipient_email)
            print(f"Email successfully sent for Day {day_number:02d} to {recipient_email}.")
        else:
            print(f"Day {day_number:02d} is not available yet.")

    except Exception as e:
        print(f"An error occurred: {e}")
