read_file = open("file1.txt",'r')
output = read_file.read()
number_of_line = sum (1 for line in read_file)
print(f"The total numbrer of lines in the file is : {number_of_line}")

read_file.close()