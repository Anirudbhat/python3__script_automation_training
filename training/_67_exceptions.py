'''
Various types of exception:
    1. NameError
    2. TypeError
    3. FileNotFoundError
    4. ZeroDivsionError
'''

#If the type of error that may occur in a block of code is known, we can write different exeptions for each type of error

try:
    #Try each of the below errors by commenting out other lines.
    #print(a)             #NameError
    #print(4+"hi")        #TypeError
    #open("tjfldsj.txt")  #FileNotFoundError
    #print(5/0)           #ZeroDivisionError
    import fabric         #ModuleNotFoundError
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Adding number and string is not possible")
except FileNotFoundError:
    print("The file trying to open is not found")
except ZeroDivisionError:
    print("Division of any number by zero is not possible")
except ModuleNotFoundError:
    print("Install module before import")
except Exception as e:
    print(e)
finally:
    print("Finally will execute after try & except is done, irrespective of occurance of error or not")
