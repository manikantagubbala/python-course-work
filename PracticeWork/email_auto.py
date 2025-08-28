#email_auto.py
import day1 as d

rec_mail = input("Enter an Email: ")
subject = input("Enter Subject: ")
body = input("Enter the Body: ")

d.send_email(rec_mail, subject, body)