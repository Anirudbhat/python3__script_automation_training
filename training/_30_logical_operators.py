# LOGICAL OPERATORS
'''
and  - Returns true if both operands are true
or   - Returns true if either of operands are true
not  - inverts the input
all  - similar to and - Returns true if all the operands are true    = syntax = all([1st operand, 2nd operand, ....])
any  - similar to or  - Returns true if any of the operands is true  = syntax = any([1st operand, 2nd operand, ....])
'''

a = eval(input("Enter the first operand"))
b = eval(input("Enter the second operand"))
c = eval(input("Enter the third operand"))

print(f"AND of {a}, {b}, {c} is {a and b and c}") 
print(f"OR of {a}, {b}, {c} is {a or b or c}") 
print(f"NOT of {a} is {not a}, NOT of {b} is {not b}, NOT of {c} is {not c}") 
print(f"ALL of {a}, {b}, {c} is {all([a, b, c])}") 
print(f"ANY of {a}, {b}, {c} is {any([a, b, c])}") 
