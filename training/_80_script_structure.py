#How to use functions from one script to another

#Whenever, there is a need to use a function from another script, it needs to be imported
#When we import any script whole of that script will get imported and if there is any code written outside functions, it will run along with current script although it is not needed
#Hence, in all the scripts entire codes should be present inside any of the functions, except for the line calling main() function.

#To call main() function, a predefined variable called '__name__' is used.
#'__name__' variable contains '__main__' as default value. But if the script gets imported by any other script, the value of '__name__' inside the script that was imported would change to the script name.

#Example: There are 2 scripts. a)script1 b)script2
#Both script1 & script2 will have implicit variable '__name__' with value '__main__' when they are created.
#If script2 imports script1, value of '__name__' in script2 will remain as '__main__'. But value of '__name__' in script1 will be changed to 'script1'(name of imported script). 
#The change of value of '__name__' variable in script1 is only applicable when it is imported and run by other scripts. When script1 itself is run, the value of '__name__" remains as '__main__'

import _80_script1

def mul(a, b):
    print(f'Multiplication of {a} and {b} is {a*b}')
    return None

def main():
    p = 8
    q = 7
    _80_script1.add(p, q)
    _80_script1.sub(p, q)
    mul(p, q)
    return None

print("Script2 name is ", __name__)

if __name__ == "__main__":
    main()
