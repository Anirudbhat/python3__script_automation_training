import my_module #Import any module by doing "import <file name without .py extension>"

print(my_module.my_value) # Use the imported file using <module_name>.<function/variable name>

import math  #math is an inbuilt module in python

print(math.pi) #pi is a function in math module

# print(help("modules"))  #Displays all the inbuilt module names

# pip install <module_name> #Used in the terminal to install the custom modules in Python

# print(help(math))   # Used to get to know about all the functions/constants in a given module

from math import *  # Used to selectively import only required functions. 
                    # Advantage of using this is that you don't need to mention module name before calling the funcion from that module
print(pi)           # Here I didn't mention module name before calling the constant as in line number 7.

from math import pow  # Selectively importing pow() function from math module

print(pow(2,3))     

import math as m      # Alias names. When you want to call function/constant from math module, you can instead call it as m. Eg given below

print(m.nan)          # Here if you call math.nan, it would result in error as math is imported using the name 'm'

#importing multiple modules in a single line

import math, subprocess, os, csv
