#Functions with default arguments

def add_num(a, b = 0):
    return a+b

def main():
    print(add_num(5,10))
    print(add_num(5))               #Since default arg of b is 0 for add_num() fn, if there is no 2nd arg, fn will take 0 as default arg
    print(add_num(9))
    return None

main()
