x = "Python"
y = "-".join(x)
print(y)
print("*".join(x))
print("\n".join(x))
print("\t".join(x))

print("#=========center=============#")
my_str1 = "Python"
my_str2 = "Python scripting"
my_str3 = "Python scripting automation"
print(my_str1.center(20))
print(f"{my_str1.center(50)}\n{my_str2.center(50)}\n{my_str3.center(50)}")

print("#================zfill================#")
print(x.zfill(10))
