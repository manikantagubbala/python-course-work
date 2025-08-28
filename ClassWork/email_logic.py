# email_logic.py

import Email_Automation

rec_mail = input("Enter Mail: ")
subject = input("Enter Subject: ")
body = input("Enter Body: ")

Email_Automation.send_email(rec_mail, subject, body)