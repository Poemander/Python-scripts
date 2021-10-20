#!/bin/python3.8

import os

# File path of the cookie file backup copied to the Document folder and actual cookie file path for Chrome in Linux

path = '/home/user/Documents/Cookies_Chrome'
new_path = '/home/user/.config/google-chrome/Default/Cookies'

# Open the cookie backup file, read and write to cookie file in chrome

cookie_file = open(path, 'rb')
data = cookie_file.read()
new_cookie_file = open(new_path, 'wb')
new_cookie_file.write(data)

# Close the files at he end

cookie_file.close()
new_cookie_file.close()
