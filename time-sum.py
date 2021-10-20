#!/bin/python3.8

import re
import datetime
import time

# Define file paths and open/read initial file

path = '/home/user/Desktop/times.txt'
new_path = '/home/user/Desktop/time_sum.txt'
time_file = open(path, 'rt')
data = limits_file.read()

# Find the times in the initial file through regular expression

match = re.findall(r'([0-9]{2}:[0-9]{2}:[0-9]{2})', data)
sum = datetime.timedelta()

# Add the times together to get sum through timedelta

for i in match:
    (h, m, s) = i.split(':')
    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    sum += d

# Print sum, add it to a file and close both files
# Sleep for 10sec so if running from file the Shell will show the result before closing
# You can delete or comment out the write to a
# separate file part of the code as well if not necessary 

print(str(sum))
new_time_file = open(new_path, 'w')
new_time_file.write(str(sum))
time_file.close()
new_time_file.close()

time.sleep(10)
