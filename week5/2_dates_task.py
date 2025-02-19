import datetime

#1st task
now = datetime.datetime.now()

year, month, day = now.year, now.month, now.day

new_day = day - 5
new_date = datetime.datetime(now.year, now.month, new_day)
print(f"5 days ago was: {new_date.strftime("%Y-%m-%d")}")

#2nd task
past = day - 1
yesterday = datetime.datetime(now.year, now.month, past)
future = day + 1
tomorrow = datetime.datetime(now.year, now.month, future)
print(f"yesterday was: {yesterday.strftime("%Y-%m-%d")}")
print(f"today is: {now.strftime("%Y-%m-%d")}")
print(f"tomorrow will be: {tomorrow.strftime("%Y-%m-%d")}")

#3rd task
print(datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second))

#4th task
import math
some_date = datetime.datetime(2006, 10, 8, 23, 59, 59)
another_date = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
difference = abs(now.second - some_date.second)
print(difference)