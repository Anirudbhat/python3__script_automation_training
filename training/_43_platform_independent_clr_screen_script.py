#!/usr/bin/python3

import os
import platform

#Clearing the terminal without depending on the type of OS
if(platform.system() == "Linux"):
    os.system("clear")
elif(platform.system() == "Windows"):
    os.system("cls")
