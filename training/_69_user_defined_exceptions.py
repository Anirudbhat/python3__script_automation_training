#User-defined exceptions

# 1. raise  - raise is used to raise existing exception wantedly
# Eg: raise Exception("This is a exception")
# raise NameError("Variable is not defined")
# raise FileNotFoundError("File is not found")

age = 20

if age > 30:
    print("valid age")
else:
    '''Uncomment below line to test raise example'''
    #raise ValueError("Age should be greater than 30")     

# 2. assert - assert <condition>
# assert will cause assertion error if the condition is false

try:
    assert age>30
    print("Valid age")
except AssertionError:
    print("AssertionError: Age should be less than 30")
