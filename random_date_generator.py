#Generate a random date between given start and end dates
from random import randrange
from datetime import timedelta,datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2012 1:30 PM', '%d/%m/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2024 4:50 AM', '%d/%m/%Y %I:%M %p')
print(random_date(d1, d2))