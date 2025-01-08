#Functions with variable length key based argument

#  **<parameter_name> is used in function declaration to have key based argument of variable length
def display(**karg):
    print(karg)
    return None

display(a = 5, b = 10, c = "gg")
