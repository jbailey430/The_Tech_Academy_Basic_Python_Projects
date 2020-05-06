
import os
import os.path
import sys
import time

path = os.getcwd()

dir_list = os.listdir(path)

print("Files and directories in '",'C:\The-Tech-Academy-Basic-Python-Projects\', "')
print(dir_list)


fPath = 'C:\\The-Tech-Academy-Basic-Python-Projects\\'

for fPath in os.listdir(path='C:\\The-Tech-Academy-Basic-Python-Projects\\'):

    if (fPath.endswith('.txt')):
        print(fPath)
        print(os.path.getmtime('C:\\The-Tech-Academy-Basic-Python-Projects\\'))
        continue
    else:
        continue





