#findall, finditer in regex

#findall will search the pattern and give all the matched patterns output as a list. If no pattern matches, empty list will be given.

#finditer will search the pattern and give all the matched patterns as output with starting and ending index(same format as output of search() fn). Even if no match happens, there will be output.

import re

text = "This is python . we have python2 and python3 versions. Future version is python4"
pattern = r"\bpython\d*\b"

print("findall output:", re.findall(pattern, text))


for each_ob in re.finditer(pattern,text):
    print("finditer output:", each_ob)
