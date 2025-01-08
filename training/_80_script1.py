def add(a, b):
    print(f"Addition of {a} & {b} is {a+b}")
    return None

def sub(a, b):
    print(f"Subtraction of {a} from {b} is {a-b}")
    return None

def main():
    x = 10
    y = 9
    add(x, y)
    sub(x, y)
    return None

print("Script1 name is ", __name__)

if __name__ == "__main__":
    main()
