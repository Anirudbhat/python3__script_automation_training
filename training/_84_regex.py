'''
Rules to create pattern
-----------------------
1. ^     => Start of the string (Start of line in case of multiline string)
2. $     => End of the string   (End of line in case of multiline string)
3. \b    => Empty string at beginning or end of word (blank space)
4. \B    => No empty string at beginning or end of word (No blank space)
5. \t, \n, \r  ==> Matches tab, newline, return respectively.
-----------------------
'''

import re

text_1 = "it is a python learn and it is easy to learn"
my_pat_1 = "^it is"            # By using ^, we ensure pattern matches only if it is at beginning of line
print("1--", re.findall(my_pat_1, text_1))

my_pat_2 = "learn$"            # By using $, we ensure patten matches only if it is at end of line
print("2--", re.findall(my_pat_2, text_1))


text_3 = "it is a pythonlearn learn and it is easy to learnn"
my_pat_3 = "\\blearn\\b"            # By using \b at beginning and end of word, we ensure pattern matches only if there are empty space at either side of word. 2 backslashes are used before b because, there is already \b used in string to indicate backspace
print("3--", re.findall(my_pat_3, text_3))
my_pat_3_1 = r"\blearn\b"           # If we mention the string as raw by writing r before starting the string, then we no need to put 2 backslashes while using \b
print("3.1--", re.findall(my_pat_3, text_3))



text_4 = "it is a pythonlearn nlearnn and it is easy to learnn"
my_pat_4 = "\Blearn\B"            # By using \B at beginning and end of word, we ensure pattern matches only if there are NO empty space at either side of word. 
print("4--", re.findall(my_pat_4, text_4))
