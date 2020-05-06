
import os
import os.path
import sys
import time

path = os.getcwd()

dir_list = os.listdir(path)

print("Files and directories in '",'C:\The-Tech-Academy-Basic-Python-Projects\', "')
print(dir_list)


fName = 'test.txt, test2.txt'

fPath = 'C:\\The-Tech-Academy-Basic-Python-Projects\\'

data = ["test.txt", "test2.txt"]
for x in data:
    print(x)
    if x == "test2.txt":
        break


abPath = os.path.join(fPath, fName)
print(abPath)



path = 'C:\\The-Tech-Academy-Basic-Python-Projects\\'
try:
    modification_time = os.path.getmtime(path)
    print("Last modification time since the epoch:", modification_time)

except OSError:
    print("Path '%s' does not exsists or is inaccessible" %path)
    sys.exit()

local_time = time.ctime(modification_time)
print("Last modification time (Local time):", local_time)

