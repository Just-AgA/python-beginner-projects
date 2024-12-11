#Subtract a week (7 days)  from a given date in Python
from datetime import datetime, timedelta

#Use the timedelta() function to subtract days from a given date

print("Given date:")
given_date = datetime(2020, 2, 25)
print(given_date)

new_date = given_date - timedelta(days=7)
print("New date:")
print(new_date)