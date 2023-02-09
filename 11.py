'''11.FILES
1. Write a program to read text file
2. Write a program to write text to .txt file using InputStream
3. Write a program to read a file stream
4. Write a program to read a file stream supports random access
5. Write a program to read a file a just to a particular index using seek()
6. Write a program to check whether a file is having read access and write access permissions

Here is a sample program that demonstrates the different operations you asked for:'''


# Reading a text file
with open("text_file.txt", "r") as file:
    content = file.read()
    print("Content of text file:")
    print(content)

# Writing text to a .txt file using InputStream
text = input("Enter text to be written to file:")
with open("text_file.txt", "w") as file:
    file.write(text)
    print("Text written to file.")

# Reading a file stream
with open("text_file.txt", "r") as file:
    content = file.read(10)
    print("First 10 characters of the file:")
    print(content)

# Reading a file stream that supports random access
with open("text_file.txt", "r") as file:
    file.seek(5)
    content = file.read(10)
    print("Characters from index 5 to 14:")
    print(content)

# Reading a file at a particular index using seek()
with open("text_file.txt", "r") as file:
    file.seek(15)
    content = file.read(1)
    print("Character at index 15:")
    print(content)

# Checking file permissions
import os
file_name = "text_file.txt"
print("Read permission:", os.access(file_name, os.R_OK))
print("Write permission:", os.access(file_name, os.W_OK))
#This program demonstrates how to read a text file and write text to it using InputStream. It also demonstrates how to read a file stream and a file stream that supports random access, as well as how to read a file at a particular index using the seek() method. Finally, it demonstrates how to check if a file has read and write access permissions using the os.access() method.