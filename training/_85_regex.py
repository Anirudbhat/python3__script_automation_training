'''
Rules to create a pattern:
-------------------------
1. {2}         -> Matches repeating of 2 times.
2. {2, 4}      -> 2,3 or 4 times.
3. {2, }       -> 2 or more times.
4. +           -> 1 or more times.
5. *           -> 0 or more times.
6. ?           -> once or none. (lazy)

Note: Above repeating terms will match for only the preceding character but does not match the whole word. 
abc{2}   -> This will match to abcc (not abcabc).
-------------------------
'''
import re

text = "xaz axdfa sdf xaaz xaaaaaz xaaaaaaaaz xz"

my_pat_1 = r"\bxa{2}z\b"
print("1-->\t", re.findall(my_pat_1, text))

my_pat_2 = r"\bxa{2,5}z\b"
print("2-->\t", re.findall(my_pat_2, text))

my_pat_3 = r"\bxa{2,}z\b"
print("3-->\t", re.findall(my_pat_3, text))

my_pat_4 = r"\bxa+z\b"
print("4-->\t", re.findall(my_pat_4, text))

my_pat_5 = r"\bxa*z\b"
print("5-->\t", re.findall(my_pat_5, text))

my_pat_6 = r"\bxa?z\b"
print("6-->\t", re.findall(my_pat_6, text))
