#email_auto.py
import day1

rec_mail = input("Enter an Email: ")
subject = input("Enter Subject: ")
body = input("Enter the Body: ")

day1.send_email(rec_mail, subject, body)