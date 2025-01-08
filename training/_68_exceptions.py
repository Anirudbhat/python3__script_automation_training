#try-except-finally & try-except-else block

try:
    a = 9
    print(a)
except NameError:
    print("Variable is not defined")
except Exception as e:
    print(e)
else:   #optional
    print("This will execute only when there is no error/exception in try block")
finally:#optional
    print("This will always execute")
