#Functions: Functions is used to make the codes more reusable, modular & readable
#2 types: Built-in & user-defined

#Scope of variables: LOCAL & GLOBAL
#Local variables: Local variables are those which are declared inside any function and useable by only the function within which it is declared.
#Global variables: Global variables are those which are either declared outside the functions or declared as 'global' within the function. These variables can be used by any function even if the function has not declared that variable.


def my_function_1():
    x = 60           #local variable
    print("my_function_1", "x=", x, "y=", y)
    my_function_2()
    return None

def my_function_2():
    print("my_function_2", "x=", x, "y=", y)
    return None

def main():                    #main() function is no different from any other functions. It is more of a convention to use main() fn
    global x                   #global variable
    x = 10
    my_function_1()
    return None

y = 10                         #global variable
main()
