#Sets are unordered set of items where items are unique and cannot be repeated.
my_set = {4, 3, 5, 2, 5, 2, 5, 1}
print(my_set)
print(bool(my_set))
my_empty_set = set({}) #if we don't use set() fn while creating empty set, the {} will create empty dictionary instead of set
print(type(my_empty_set), my_empty_set)
print(bool(my_set))
my_list = [8, 4, 9, 0, 2, 3, 9, 1, 1, 0, 8]
print(set(my_list))

print("=====================Available functions in a set=============================")
print(dir(my_set))

print("=======================Union-intersection======================")
a = {2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9, 10}
print(a.union(b))
print(a.intersection(b))
