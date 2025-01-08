#Functions with variable length argument

def display(*data):
    for each in data:
        print(data, type(each))
    return 0

display(8)
display(4, 6, 98)
display("hardik", 69)
