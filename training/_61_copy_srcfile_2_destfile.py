src_file = input("Enter the path of source file")
dest_file = input("Enter the pathof dest file")

src_fo = open(src_file, "r")
content = src_fo.read()
src_fo.close()

dest_fo = open(dest_file, "w")
dest_fo.write(content)
dest_fo.close()
