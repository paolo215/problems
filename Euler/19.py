#Counting sundays
import datetime

count = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if datetime.datetime(i, j, 1).weekday() == 6:
            count += 1

print count
