my_empty_dict = {}
print(my_empty_dict, type(my_empty_dict))
print(bool(my_empty_dict))

print("==================get_a_variable_using_key==================")
my_dict = {'fruit':'apple', 'animal':'fox', 1:'one', 'two':2}
print(my_dict)
#Difference between the below 2 methods is that, in the 1st method below, if the given key is not present in the dictionary there will be error.
#In the 2nd method(get() fn), If the given key is not present, output will be None.
print(my_dict['fruit'])  #Output will be the respective variable(In this case,'apple') associated with the specified key(In this case, 'fruit')
print(my_dict.get('animal'))  #Output will be the respective variable(In this case,'fox') associated with the specified key(In this case, 'animal')
#print(my_dict[3])   #This will result in error as 3 is not a key inside my_dict dictionary
print(my_dict.get(3))   # This will give None as output as 3 is not  a key inside my_dict dictionary

print("========================clear==========================")
print(my_dict)
my_dict.clear()  #This function deletes all the variable/keys in this dictionary
print(my_dict)

print("==============Assigning a new key variable to a given dictionary===============")
my_dict = {'fruit':'apple', 'animal':'fox', 1:'one', 'two':2}
print(my_dict)
my_dict["three"] = 3  #When a variable is assigned using the given key, if the key is not already present in the dictionary, a new key variable pair will be created
print(my_dict)
my_dict["three"] = 38 #When a variable is assigned using the given key, if the key is already present in the dictionary, the new variable will be assigned to the given key
print(my_dict)

print("==================keys-values-items-copy=================")
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
y = my_dict.copy()
print(y)
print(id(my_dict), id(y))

print("=========================update==========================")
my_new_dict = {'four': 4}
my_dict.update(my_new_dict)  #This function will add my_new_dict into my_dict
print(my_dict)

print("======================pop-popitem=====================")
print(my_dict.pop('four')) #Deletes item based on the given key
print(my_dict)
removed_item = my_dict.popitem() #Randomly removes an item
print(my_dict)
print(removed_item)


print("=======================fromkeys=======================")
keys = [1, 2, 3, 4, 5, 6, 7]
new_dict = dict.fromkeys(keys) #fromkeys() fn is used to create a dict using a list of keys.
print(new_dict)
new_dict[1] = "First value"
print(new_dict)

print("=======================setdefault====================")
#setdefault() will set default values for any key if the key is not present in the dictionary else if key is present, it will not change anything.
my_dict = {}
my_dict.setdefault('k', 45)
print(my_dict)
my_dict = {'fruit': 'apple'}
my_dict.setdefault('fruit', 'orange')
print(my_dict)
