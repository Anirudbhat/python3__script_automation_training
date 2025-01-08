#!/usr/bin/python3

import os

#os.system() function is used to use system commands

os.system("pwd")
os.system("date")
cmd1 = os.system("pwd")         #When os.system() is assigned to any other variable, it will not assign o/p to the variable, instead it will assign the return value to the variable, In most cases it would be 0
cmd2 = os.system("jdlfjkd")

if cmd1 == 0:
    print("cmd1 is a valid command")
else:
    print("cmd1 is an invalid command")

if cmd2 == 0:
    print("cmd2 is a valid command")
else:
    print("cmd2 is an invalid command")
