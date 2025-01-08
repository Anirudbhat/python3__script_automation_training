#!/usr/bin/python3

import os

req_path = input("Enter the path of file/directory: ")

if(os.path.exists(req_path)):
    if(os.path.isfile(req_path)):
        print("Entered path is of a file")
    else:
        print("Given path is a directory")
else:
    print("Given path doesn't exist")

