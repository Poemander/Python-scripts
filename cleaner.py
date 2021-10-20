#!/bin/python3.8

import os

# First clean all unwanted cookies manually (I know a bit of a pain), after go to 
# ~/.config/google-chrome/Default/Cookies and copy the file to your Documents folder.
# Now whenever you run this code it'll replace the cookies file in chrome with the clean one

# replace '<user>' with your username

path = '/home/<user>/Documents/Cookies_Chrome'
new_path = '/home/<user>/.config/google-chrome/Default/Cookies'

# Open the cookie backup file, read it and write it to the cookie file in chrome

cookie_file = open(path, 'rb')
data = cookie_file.read()
new_cookie_file = open(new_path, 'wb')
new_cookie_file.write(data)

# Close the files at he end

cookie_file.close()
new_cookie_file.close()
