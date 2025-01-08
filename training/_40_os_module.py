#!/usr/bin/python3

import os

print(os.getcwd())  #Gets current working directory
print(os.listdir())  #Returns a list containing the names of files in directory
print(os.getrandom())

my_path = "home/aniruddha/python3/training/_40_os_module.py"
my_second_path = "home/aniruddha/python3/training/"

print(f'Basename of my_path is {os.path.basename(my_path)}')  #os.path.basename gives the ending file/folder in a given path
print(f'Basename of my_second_path is {os.path.basename(my_second_path)}')  #If the pathname ends with '/' then the o/p is null

print(f'dirname of my_path is {os.path.dirname(my_path)}')  #os.path.dirname gives the path excluding ending file name
print(f'dirname of my_second_path is {os.path.dirname(my_second_path)}')  #If the pathname ends with '/' then the o/p is full path

path1 = "/home"
path2 = "aniruddha"

print(os.path.join(path1, path2))     #os.path.join function joins the path with correct seperator irrespective of the OS we are using

print(os.path.split(my_path))        #os.path.split is used to split the basename and dirname in a given path. O/p will be tuple

my_path = "/home/aniruddha/python3/training"
print(os.path.getsize(my_path))      #os.path.getsize will give the size inside the given path

if os.path.exists(my_path):              #os.path.exists() is used to check if a given path does exist or not?
    print(f'{my_path} does exist')
else:
    print(f'{my_path} doesn\'t exist')

if os.path.isfile(my_path):              #os.path.isfile() is used to check if a given path is of a file or not
    print(f'{my_path} is a file')
else:
    print(f'{my_path} isn\'t a file')

if os.path.isdir(my_path):              #os.path.isdir() is used to check if a given path is of a dir or not
    print(f'{my_path} is a directory')
else:
    print(f'{my_path} isn\'t a directory')

if os.path.islink(my_path):              #os.path.isdir() is used to check if a given path is a soft link
    print(f'{my_path} is a soft link')
else:
    print(f'{my_path} isn\'t a soft link')

