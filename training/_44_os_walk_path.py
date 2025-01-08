#!/usr/bin/python3

import os

#os.walk(path) is used to get all the files, folders, all the subfiles & subfolders
#The output will be list of tuples with each tuple representing a directory.
#Each tuple will have 3 lists, 1st list contain path, 2nd list contains folders in that path, 3rd list contains files in that path.

path = "/home/aniruddha/python3"
print(list(os.walk(path)));
print("====================================Printing each element(path, folder, file) of the tuple seperately======================================")
for r,d,f in os.walk(path):     #Printing each element(path, folder, file) of the tuple seperately
    print(r,"\n")
    print(d,"\n")
    print(f,"\n")
    print("---------------------------------------------------")

for r,d,f in os.walk(path):      #Processing the output from os.walk(path)
    if len(f) != 0:
        print(r)
        for each_file in f:
            print(os.path.join(r, each_file))
            print("_____________________________")
