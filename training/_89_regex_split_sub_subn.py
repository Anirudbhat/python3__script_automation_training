#split-sub-subn-functions

#split - This function will split the given text wherever the pattern matches

#sub - This function will substitute the given text with the required pattern

#subn - This function will substitute the given text with the required pattern. Output is a tuple(output also contains no. of replaces made).

import re

my_str = "This is python and pytHon is very easy. present python versions are pytHon1 & Python2"
my_pat = r"python"

print("1-->", re.split(my_pat, my_str))             #this doesn't include case ignorecase flag.
print("2-->", re.split(my_pat, my_str, flags = re.I))  #contains case ignorecase flag

print("3-->", re.sub(my_pat, "Java", my_str, flags = re.I))    #Replacing python by Java
print("4-->", re.sub(my_pat, "Java", my_str, count = 1, flags = re.I))    #Replacing python by Java for only 1 time


print("4-->", re.subn(my_pat, "Java", my_str, flags = re.I))    #Replacing python by Java
print("5-->", re.subn(my_pat, "Java", my_str, count = 1, flags = re.I))    #Replacing python by Java for only 1 time
