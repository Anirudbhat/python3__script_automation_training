# IDENTITY OPERATORS
# is used to compare the type of 2 variables
"""
is
is not
"""

#MEMBERSHIP OPERATORS
# is used to check if a variable is present in a list/other data structures
"""
in
not in
"""

print("# IDENTITY OPERATORS")
a = 8
b = 927
c = "lfkdj"
print(type(a) is type(b))
print(type(a) is not type(b))
print(type(a) is type(c))
print(type(a) is not type(c))


print("#MEMBERSHIP OPERATORS")
a = ['l', 'kdj', 'd', 'k']
print('l' in a)
print('fkd' in a)
