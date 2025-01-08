# COMPARISION OPERATORS

""" <, >, ==, !=, <=, >= """

# We can use strings as operands with comparision operators too. If strings are used, the respective ASCII value of the string will be compared.
#ord() function will return the ASCII value of string. chr() function will return string variable for the given ASCII value.
#If there is an array of values in string, then comparision happens from leftmost variable of one string with leftmost variable of other string.

a = eval(input("Enter first number = "))
b = eval(input("Enter second number = "))
print(f'lessthan operation of {a} & {b} results in {a<b}')
print(f'greaterthan operation of {a} & {b} results in {a>b}')
print(f'equalto operation of {a} & {b} results in {a==b}')
print(f'notequal operation of {a} & {b} results in {a!=b}')
print(f'lessthan/equalto operation of {a} & {b} results in {a<=b}')
print(f'greaterthan/equalto operation of {a} & {b} results in {a>=b}')
