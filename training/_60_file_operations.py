#Working with files
#File can be opened in 3 modes: "w"-write, "a"-append, "r"-read
fo = open("demo.txt", "w")
print("file mode:", fo.mode)
print("Is file readable:",fo.readable())
print("Is file writable:",fo.writable())
fo.close()
#Opening file in write mode: Will enable us to write to the file. If file with the same name is already present in the folder, then the script will replace it with the new file. If file is not present in the folder, script will create new file when using "w" as the mode
fo = open("demo.txt", "w")
fo.write("This is the first line\n")
fo.write("This is the second line\n")
fo.write("This is the third line")
fo.close()
#writing to a file also can be done by saving all the lines to be written to the file in a list and then passing the list to file.writelines() function
#2nd method to write a saved list to a file is to iterate through each item in a list and write it to the file. 
#Method 1 - writelines() function
my_content = ["1st line\n", "2nd line\n", "3rd line"]
file = open("trash.txt", "w")
file.writelines(my_content)
file.close()
#Method 2 - iterate through each item of list 
#This method has advantage over 1st method as here we don't need to write \n at the end of each line in the list. It can be written while iterating as we have done it below
my_content = ["1st line", "2nd line", "3rd line"]
file = open("trash2.txt", "w")
for each_item in my_content:
    file.write(each_item+"\n")
file.close()


#APPEND MODE: In append mode, if the opened file doesn't exist in the given folder, then the append function will create a new file and write to it.
#If Opened file name already exists in the given folder, then the append function will start writing from the last line of the existing file.
my_content = ["1st line", "2nd line", "3rd line"]
file = open("trash3.txt", "a")
for each_item in my_content:
    file.write(each_item+"\n")
file.close()

#READ MODE:
#Read mode is used to read the content from file. 
#Content can be read in 2 ways - 1. Read all the lines at once. 2. Read a single line
fo = open("trash.txt", "r")
read_data = fo.read()
fo.close()
print("Read data from trash.txt file:\n", read_data)

#Reading a single line
fo = open("trash.txt", "r")
print("Reading a single line 1st time:", fo.readline())
print("Reading a single line 2nd time:", fo.readline())
fo.close()

#Reading the data from the file and storing it as list using readlines() fucntion
fo = open("trash.txt", "r")
read_data_list = fo.readlines()
fo.close()

for each_line in read_data_list:
    print("Printing each line in list:", each_line)

