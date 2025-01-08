# TUPLES ARE IMMUTABLE LIKE STRING.
my_empty_tuple = ()
print(my_empty_tuple)
my_tuple = (1, 2, 3)
print(my_tuple)


print("======================convert-to-bool========================")
print(bool(my_empty_tuple))
print(bool(my_tuple))

my_tuple = (3, 4, [3, 5, 4], 9)
print(my_tuple)


print("============Accessing elements using index================")
print(my_tuple[2])
print(my_tuple[2][1])

print("================Check the avail functions=================")
print(dir(my_tuple))

print("==========================count============================")
x = (3,4,2,5,0,1,3)
print(x.count(3))  #Output of 'count' function will be the number of times given arg is repeated in the tuple
print(x.count(8))

print("===========================index===========================")
print(x.index(3))  #output is the index number of given arg in the tuple. (If there are multiple args in tuple, output will be index of 1st repetition
print(x.index(3, 2))  #1st arg is the variable to be searched, 2nd arg is the index from which search should begin

print("============================len==========================")
print(len(x))  #len() function can be used to find the size of string, list & tuple

print("====================Selective printing of tuple==================")
print(x[:5])
print(x[3:])

print("==============Ways to initialize tuple===================")
y = 5,
z = 3, "fdlj", 3
print(y, type(y))
print(z, type(z))
