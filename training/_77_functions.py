#Functions with keyword as argument

def display(a,b):
    print(f"value of a is {a}")
    return None

display(a = 3, b = 4)              #Although positions of values interchanges in the below line, since keywords also got interchanged, the output will remain same
display(b = 4, a = 3)
