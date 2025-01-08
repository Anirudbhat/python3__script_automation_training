import csv

req_file = "demo_2_.csv"
#To create and write to a csv file, we need to use writer() & writerow() function in the below given way. 
#writerow() is used to write single row. writerows() is used to write multiple rows at a time.
fo = open(req_file, "w", newline = "")
csv_writer = csv.writer(fo, delimiter = ",")
csv_writer.writerow(["sl_no", "name", "age"])
csv_writer.writerow([1, "John", 23])
csv_writer.writerow([2, "Raju", 28])

my_data = [[3, "vaik", 24], [4, "kdjfkjl", 98]]
csv_writer.writerows(my_data)
fo.close()
