#!/bin/python3.8

# Take time values from a file and sum them up
# Example: you have a file that has some login time info

#   john logged in for 3:34:56
#   john logged in for 2:45:43
#   john logged in for 1:23:12
#   john logged in for 0:13:36

# The script takes them and prints the sum into another file 
# as well as to the terminal for 10 sec, you can delete or comment out the write to a
# separate file part of the code if not necessary 

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

print(str(sum))
new_time_file = open(new_path, 'w')
new_time_file.write(str(sum))
time_file.close()
new_time_file.close()

time.sleep(10)             # Change this if you want the terminal to show the output for less time
