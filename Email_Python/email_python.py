# Importing necessary libraries
import schedule
import time
import os
from dotenv import load_dotenv
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

password = os.getenv('MAIL_PASSWORD')
username = os.getenv('MAIL_USERNAME')

def sendMail(quote):
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    msg = MIMEMultipart()
    msg["To"] = username
    msg["From"] = username
    msg["Subject"] = "Daily Inspiration"
    msg.attach(MIMEText(quote, "html"))
    s.send_message(msg)
    del msg
    s.quit()

quotes = []
with open("quotes.txt", "r") as file:
    for line in file:
        quotes.append(line.strip())

# Scheduling the task to send an email with a random quote every minute.
schedule.every(1).minutes.do(lambda: sendMail(random.choice(quotes)))

# Continuously running the scheduler to execute pending tasks.
while True:
    schedule.run_pending()
    time.sleep(1)