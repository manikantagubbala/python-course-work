# Email_Automation.py

import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "bmanikanta1357@gmail.com"
SENDER_PASSWORD = "vjwr towe nqzw moyl"

def send_mail(to_mail, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = to_mail
        msg["Subject"] = subject
        msg.attach(MIMEText(body,"plain"))

        server = smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,to_mail,msg.as_string())
        server.quit()
        print(f"Email sent to {to_mail}")

    except Exception as e:
        print(f"Error Email {e}")


send_mail("adityamandala647@gmail.com","Amazon","Congrats! You are shortlist for interview")


