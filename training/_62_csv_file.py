import csv
#CSV file - comma seperated values 

fo = open("demo_1_.csv", "r")
content = csv.reader(fo, delimiter=",")
print("Type of content is:", type(content))
for each in content:
    print(each)
fo.close()
