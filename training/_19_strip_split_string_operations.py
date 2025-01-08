print("=============================Strip operation=============================")
x = "     python      "
print(x)
print(x.strip())
x = "python"
print(x.strip("p"))
print(x.strip("n"))
print(x.strip("t")) # Strip() function will only strip the given word/letter if it is it in the either end of string
x = "Python scripting is easy"
print(x.strip("easy"))
x = x + " Python"
print(x)
print(x.rstrip("Python")) #right strip
print(x.lstrip("Python")) #left strip
print(x.strip("Python"))


x = "Pythonyy"
print(x.strip("P").strip("y"))  #Multiple strip functions

print("\n\n\n=============================Split operation=============================")
x = "Python is easy"
print(x.split())
print(x.split("is"))
x = x + " " + "and it is very popular"
print(x.split("is"))
