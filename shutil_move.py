import shutil
import os

source = '/Users/JAKEBAILEY30/Desktop/Folder_A'

destination = '/Users/JAKEBAILEY30/Desktop/Folder_B'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
