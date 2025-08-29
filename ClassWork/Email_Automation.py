# Email_Automation.py

import smtplib      # Simple Mail Transfer Protocol for sending emails
import os           # For file path and file existence checks
import csv          # To read email addresses from a CSV file
from email.mime.multipart import MIMEMultipart
# For creating multipart email messages

from email.mime.text import MIMEText
# For adding plain text to email body

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587    # Port used for TLS (encryption)
SENDER_EMAIL = "bmanikanta1357@gmail.com"
SENDER_PASSWORD = "vjwr towe nqzw moyl"

def send_email(to_email, subject, body):
    try: 
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()

        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Error sending email to {to_email}: {e}")

