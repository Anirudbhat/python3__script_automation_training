#Errors are of 2 types:
# 1. Syntax Error
# 2. Runtime Errors -> Exceptions - Can handle runtime errors using 'try{} except{}' method

#In the below example, reading error.txt file should result in error and stop simulation as there is no file named 'error.txt'
#But since we have used it in try except block, if some error occurs in 'try' block, execution stops in 'try' block & 'except block will be executed
try:
    fo = open("error.txt")
    print(fo.read())
    fo.close()
except:
    print("Problem while reading error.txt file")

#We can also print the 'Error' that caused exception using the method below
try:
    fo = open("error.txt")
except Exception as e:
    print("The error that caused exception is:", e)
    
#Probable causes of exceptions
'''
1. index error
2. Zero division error
3. import error
4. Value error
5. Type error
6. Name error
7. Filenotfound error
'''
