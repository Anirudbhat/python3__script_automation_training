import csv
#CSV file - comma seperated values 
#Read only header of csv file and count number of rows in csv file

#2 ways to get the header of content, 
#Method 1 - By converting read data to list and getting '0th' index of that list
fo = open("demo_1_.csv", "r")
content = csv.reader(fo, delimiter=",")
print("Header of content is:", list(content)[0])
fo.close()

#Method 2 - By using next() function(next() function is used to move cursor to next line)
fo = open("demo_1_.csv", "r")
content = csv.reader(fo, delimiter=",")
print("Header of content is:", next(content))

#counting number of rows. - Can be done by len(content)
print("Number of rows is:", len(list(content))) 
#Here, Number of rows will be displayed as 2 even though there are 3 rows, because in previous line we used next() function which will move cursor to second line. So, the len() function will check the length starting from 2nd line


fo.close()
