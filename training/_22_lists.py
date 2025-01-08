my_list1 = []
print(bool(my_list1))  #bool(empty_list) -> False
my_list2 = [3, 2, 4, "python", 5.6]
print(bool(my_list2))  #bool(non-empty-list) -> True
print(my_list2, type(my_list2))
print(my_list2[0])
print(my_list2[3])
print(my_list2[-1])
print(my_list2[3][3]) #To print an index of string which is inside a list

print("=============All 3 below statements print the complete list===========")
print(my_list2)
print(my_list2[:])
print(my_list2[0:])

print("==============Selective printing of list===========")
print(my_list2[1:4])

print("============== Assigning a new element to an index in a list===========")
my_list2[0] = 434  # Lists are mutable and strings are immutable
print(my_list2)

# Display all the in-built functions available for lists - !!Only use the once without underscores. The ones with underscores aren't usable
#print(dir(my_list2))


print("#=======================Funtions on list==============================#")
print("=======================index=====================#")
x = [0,1,2,3,4,5,4,3,2,1]
print(x.index(5))
print(x.index(4,5)) # 1st argument is the value we are searching, 2nd argument is the index after which we want to search the given argument.


print("#=======================count=====================#")
print(x.count(4)) # Gives the number of times element is repeated in the list


print("=======================clear=====================#")
# Operations which modify the given list should not be used directly with print. The modification should be done seperately before printing it.
x.clear() # Deletes all the element in the list
print(x) 


print("=======================copy=====================#")
my_list1 = x          # This assignment would make my_list1 point to the same location of x. Any changes made to x would reflect on my_list1 and viceversa
print(id(x), id(my_list1))  # id() function would return the mem location of any variable
my_list2 = x.copy()   # This assignment would copy the contents of x to different location and my_list2 handle will point to this new location. Any changes made to x is not reflected in my_list2 and viceversa
print(id(x), id(my_list2))


print("==================append-insert=================")
x = [0,1,2,3,4,5,4,3,2,1]
print(x)
x.append(56)    #Append would add an element at the end of given list
print(x)
x.insert(1, 99)  #Insert would add the element in the given index. - 1st arg is index you want to add your element, and 2nd arg is the element you want to add
print(x)


print("=====================extend======================")
x = [0,1,2,3,4,5,4,3,2,1]
print(x)
my_new_list = [99, 88]
x.extend(my_new_list)  # Extend is used to concatenate 2 lists
print(x)


print("==================remove-pop===================")
x = [0,1,2,3,4,5,4,3,2,1]
print(x)
x.remove(5) # remove functions would remove the given value from the list. If the given value is not in the list, it would pop error. Hence when using remove fn, we always need to use conditional statement(if-else)
print(x)

x.pop()  # 'pop' function without any arg will remove last element from the list
print(x)
x.pop(0) # arg given here is the index that needs to be removed from the list. Here pop fn would remove element in the 0th index of this list
print(x)
print(x.pop(2)) # Using 'pop' fn inside print would print the value that is removed by 'pop' fn
print(x)


print("==================reverse-sort=================")
x = [4,8,3,7,2,0]
print(x)
x.reverse()
print(x)
x.sort()  #sort will be done in ascending order
print(x)
x.sort(reverse = True)  #sort in descending order
print(x)
