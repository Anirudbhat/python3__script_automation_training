#!/usr/bin/python3

#break is used to stop the loop completely
#continue is used to stop the current iteration and move to next iteration in a loop.
#pass is used in empty loops when loops are not assigned any values

for i in range(5):
    print(i)
    if(i == 3):
        break

print("Break loop complete, starting continue loop")

for j in range(8):
    if(j%2 == 0):
        print(j)
    else:
        continue

print("continue loop complete, starting pass loop")

for k in range(9):
    pass
