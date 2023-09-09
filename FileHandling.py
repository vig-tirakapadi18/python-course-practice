# Reading a file
my_file = open("FileHandling1.txt", 'r')
print(my_file.read())
my_file.close()

# Writing to a file - Using 'w', It will remove all the existing data and writes a new data
my_file = open("FileHandling1.txt", 'w')
print(my_file.write("Hello Bello Hello!"))
my_file.close()

# Writing to a file = Using 'a', It will write without removing existing data
my_file = open("FileHandling1.txt", 'a')
print(my_file.write(" I am doing great, How are you doing?"))
my_file.close()

# Copying text from one file to another file
my_file1 = open("FileHandling1.txt", 'r')
my_file2 = open("FileHandling2.txt", 'w')

for i in my_file1:
    print(my_file2.write(i))

my_file2.close()
