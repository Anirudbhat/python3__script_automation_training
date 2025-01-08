#Compile operation in regex

#Whenever there are multiple regex operations done with the same pattern, compile operation can be used to make the operation faster and make code more efficient

import re

my_str = "This is about Python. Python is easy to learn. There are 2 major versions of python: Python2 & Python3"

my_pat = r"\bpython[23]?\b"

#Note:
#re.findall(my_pat, my_str) ==> re.compile(my_pat).findall(my_str)

pat_ob = re.compile(my_pat, flags = re.I)
print("1-->", pat_ob.findall(my_str))
print("2-->", pat_ob.search(my_str))
