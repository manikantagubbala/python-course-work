#Date_and_Time
'''
import datetime

to_day = datetime.date.today()
t_ime = datetime.datetime.now()
print(to_day, t_ime)
'''

from datetime import date, time, datetime

to_day = date.today()

print("Present Date: ", to_day)
#Weekday is sts from 0 
#IsoWeekday is sts from 1
print(f"Year: {to_day.year} \nMonth: {to_day.month} \nDate: {to_day.day} \nWeekday: {to_day.weekday()} \nisoWeekday: {to_day.isoweekday()}")

d=date(2004,11,16)
print("Assign a Date: ",d)
print()

specific_time = time(22,53,59)
print("Secific time: ", specific_time)
print(f"Hours: {specific_time.hour} \nMinutes: {specific_time.minute} \nSeconds: {specific_time.second}")

print()
current_date_time = datetime.now()
print("Present Date and Time: ", current_date_time)
print(f"Hour: {current_date_time.hour} \nMinutes: {current_date_time.minute} \nSeconds: {current_date_time.second} \n")

specific_date_time = datetime(2004,11,16,17,16,16)
print("Specific Date&Time: ",specific_date_time)