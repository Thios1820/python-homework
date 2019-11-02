from os.path import isfile, join  # importing package
import os  #

desktop_path = '/Users/thiorofaty/Desktop'  # Desktop path variable
content = os.listdir(desktop_path)   # list of desktop content

for i in content:
    full_path = join(desktop_path, i)  # joining desktop path and filename
    if isfile(full_path): # checking if element is a file
        print (i, 'is a file')
    else:
        print(i, 'is a directory')


