#!/usr/bin/python3

#range(start_value, stop_value, step) -> syntax of range() function

print("range(5)",range(5))
print("range(5)",list(range(5)))
print("range(0,5)", list(range(0,5)))
print("range(0,5,1)", list(range(0,5,1)))
print("range(0,20,1)", list(range(0,20,1)))
print("range(0,20,2)", list(range(0,20,2)))
print("range(0,20,3)", list(range(0,20,3)))
print("range(10,2)", list(range(10,2)))
print("range(10,2,-1)", list(range(10, 2, -1)))

my_list = [898, 927, 97, 298, "ldjfl", "jkdj"]

for each_index in list(range(len(my_list))):
    print(f"Index --> {each_index}:value --> {my_list[each_index]}")
