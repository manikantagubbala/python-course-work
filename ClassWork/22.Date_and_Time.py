#Date_and_Time
'''
import datetime

to_day = datetime.date.today()
t_ime = datetime.datetime.now()
print(to_day, t_ime)

'''
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

c_dt = datetime.now()
formatted_date = c_dt.strftime("%d/%m/%Y")                      #%Y gives 2023 and %y gives 23
print("Formatting the Date: ",formatted_date)
formatted_time = c_dt.strftime("%H:%M:%S")
print("Formatting the Time", formatted_time)
print("Normal time in hour: ", c_dt.strftime("%I:%M %p"))
print("Day with DayName: ", c_dt.strftime("%A"))
print("Month with MonthName: ", c_dt.strftime("%B"))
passing_year = date(2025,5,25)
print("Passed Out Year in Btech: ",passing_year.strftime("%b,%Y"))

'''

from datetime import date, time, datetime, timedelta

yyyy = int(input("Enter a year: "))
mm = int(input("Enter a Month: "))
dd = int(input("Enter a date: "))
dob = date(yyyy,mm,dd)
#print("Day of the given date: ", dob.strftime("%A"))

#print("Original date: ",dob)
#print("Add 15 days to given date: ", dob + timedelta(days=15))

hours = int(input("Enter hours: "))
mintues = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))
future_time = datetime(yyyy,mm,dd, hours,mintues,seconds)
present_dt = datetime.now()

print("Remaining time: ", present_dt - timedelta(future_time))