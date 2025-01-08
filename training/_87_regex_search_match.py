#search() and match() functions in regex
"""
search() will search and return only the first occurance of the searched pattern. (irrespective of single line or multiline)
match() will match and return the match object if pattern matches starting pattern of the string(in case of single line) or starting pattern of the first line(incase of multiline) 
"""

import re

text_1 = """This is python. 
THere are 2 versions of python, 
python2 and python3. 
Future is python4"""

pat = r"\bpython[23]?\b"
search_ob = re.search(pat, text_1)

if search_ob:                                              #If the searched pattern is not found, search_ob will be equal to None. Hence while using search_ob, we should always check if it is none or not.
    print("search: search_ob = ", search_ob)
    print("search: Match from pattern:", search_ob.group())
    print("search: Starting index:", search_ob.start())
    print("search: Ending index:", search_ob.end()-1)
    print("search: Lenght of pattern", search_ob.end() - search_ob.start())
else:
    print("No match found")


#===================Match=====================
text_2 = """python is python. 
THere are 2 versions of python, 
python2 and python3. 
Future is python4"""

pat = r"\bpython[23]?\b"
match_ob = re.match(pat, text_2)

if match_ob:                                              #If the matched pattern is not found, match_ob will be equal to None. Hence while using match_ob, we should always check if it is none or not.
    print("match: match_ob = ", match_ob)
    print("match: Match from pattern:", match_ob.group())
    print("match: Starting index:", match_ob.start())
    print("match: Ending index:", match_ob.end()-1)
    print("match: Lenght of pattern", match_ob.end() - match_ob.start())
else:
    print("No match found")
