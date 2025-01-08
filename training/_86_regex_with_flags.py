#Regex with flags

'''
Simple flags for regex:
    1. re.I (re.IGNORECASE) -> Makes the regex case insensitive.
    2. re.M (re.MULTILINE)  -> ^ and & will match the start and end of each line and not only the beginning and end of the string.
    3. re.L (re.LOCALE)     -> The behaviour of some special sequences like \w, \W, \b, \s will be made dependent on current locale.
    4. re.S (re.DOTALL)     -> The dot will match every character as before plus newline character.
    5. re.U (re.UNICODE     -> Makes \w, \W, \b, \s, \S dependent on unicode properties.
'''

import re

text_1 = "this is a string. This is a new string. THIS"
my_pat_1 = r"this"
print("1-->", re.findall(my_pat_1, text_1, re.I))  # re.I will make sure that regex is case insensitive.

text_2 = """this is a string
This is second line
THIS is third line
this is fourth line"""
my_pat_2 = r"^this"                # Here newline character is present in the pattern which we are checking for multiline string. If we don't use re.M flag while search the pattern, then newline character will match only at the beginning of given text.
print("2-->", re.findall(my_pat_2, text_2, re.M|re.I))       #Here 2 flags are set in findall function by using "|" symbol.
