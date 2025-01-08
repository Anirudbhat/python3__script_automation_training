print("=======================================count===================================")
x = "Python is easy and it is a popular language"
print(x.count("is"))
print(x.count("P"))
print(x.count("p"))


print("\n\n=======================================index===================================")
print(x.index("P"))
print(x.index("is"))
print(x.index("is", 8)) #1st argument to index() function is the "word whose index you need", 2nd argument is from which index you want to start the search and it is optional.
#print(x.index("is", 23)) #This will cause the error as there is no "is" word after 23rd index. Hence avoid using index() function to search index of any word in a string, instead use find() function.


print("\n\n=======================================find===================================")
x = x.lower()
print(x.find('p'))
print(x.find("p", 2))
print(x.find("p", 28))
print(x.find("p", 30)) # If the word that we are searching in the string is not found in the given string find() function will return -1
