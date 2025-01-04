#Find the day of the week of a given date
from datetime import datetime

given_date = datetime(2020, 7, 26)

#Use the weekday() method to get weekday as integer
#print(given_date.today().weekday())

#Use the strftime() method to find the name of the weekday
weekday = given_date.strftime("%A")

print("The weekday is:")
print(weekday)