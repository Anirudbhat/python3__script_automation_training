#Introduction to regular expressions (REGEX)

#Regex is a procedure in python to look for a specified pattern in a given text
#Pattern is a sequence of characters, which represents multiple strings
#EX: i[st] -> is,it

#Different operations in regex are:
#match(), search(), findall(), finditer(), sub(), split(), compile()

'''
Rules to create pattern
-----------------------
1. a, x, 9     => Ordinary characters that match themselves
2. [abc]       => Matches a or b or c.
3. [a-c]       => Matches a or b or c.
4. [a-zA-Z0-9] => Matches any letter from a to z, A to Z or 0 to 9
5. \w          => Matches any letter(a-z, A-Z), digit(0-9) or underscore(_).
6. \W          => Matches any character not part of \w like -, @, #, <space>, &, etc
7. \d          => Matches anyo decimal digit 0-9
8. .           => Matches any character other than newline character.
'''
#=================================================#

import re            # importing regex module

text_1 = "This is a python3 and it is easy to learn -- @@ -"
my_pat_1 = "is"
print("1--", re.findall(my_pat_1, text_1))        # findall() is a function within re module which will find a pattern in a given text. In this ex, my_pat_1 is being searched in text_1
print("2--", len(re.findall(my_pat_1, text_1)))
my_pat_2 = "i[ts]"                                # This pattern will expand as 'it', 'is'. Hence search will be done for both 'it' & 'is' pattern.
print("3--", re.findall(my_pat_2, text_1))        
my_pat_4 = "[a-e]"                                # Same as searching a, b, c, d, e 
print("4--", re.findall(my_pat_4, text_1))
my_pat_5 = "\w"
print("5--", re.findall(my_pat_5, text_1))
my_pat_6 = "\w\w"
print("6--", re.findall(my_pat_6, text_1))
my_pat_7 = "\W"
print("7--", re.findall(my_pat_7, text_1))
my_pat_8 = "python\d"
print("8--", re.findall(my_pat_8, text_1))
my_pat_9 = "."
print("9--", re.findall(my_pat_9, text_1))
