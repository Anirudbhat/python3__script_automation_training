#!/usr/bin/python3

import os
import sys
import datetime

age = 43 
req_path = input("Enter the req path:")

if not os.path.exists(req_path):
    print("Enter a valid path")
    sys.exit(1)

if os.path.isfile(req_path):
    print("Enter a dir path")
    sys.exit(2)

today = datetime.datetime.now()
for each_file in os.listdir(req_path):
    each_file_path = os.path.join(req_path, each_file)
    if os.path.isfile(each_file_path):
        file_cr_date = datetime.datetime.fromtimestamp(os.path.getctime(each_file_path))
        dif_days = (today - file_cr_date).days
        if dif_days > age:
            print(each_file_path, dif_days)
