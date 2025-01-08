my_string = "Python Scripting"
print(my_string.lower())
print(my_string.upper())
print(my_string.swapcase())
print(my_string) #functions called on any string will not changes the original string present in any variable.

my_new_string = "Python scripting automation"
print(my_new_string.title()) #Outputs the string with 1st letter of each word as capital

#dir() functions returns all the possible operations on any given variable.
print(dir(my_string))
