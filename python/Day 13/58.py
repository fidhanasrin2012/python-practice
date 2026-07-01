#Check file exists

import os
filename = input("Enter the filename:")

if os.path.exists(filename):
    print("File exists")
else:
    print("File doestn't exists ")