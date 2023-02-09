
 # Python Basics
"""1. Write a program to print your name.
2. Write a program for a Single line comment and multi-line comments
3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables"""

print('Gokul Subhash')
x= 1
flag= True
z= 'A'
a=3.14
b=3.13444
print("Integer",x)
print("flag",flag)
print("Character",z)
print("Float",a)
print("Double",b)


 
 # Global variable
 m = 10

 def my_func():
    # Local variable with the same name as the global variable
     m = 20
     print("Local variable x:", m)

# Calling the function
 my_func()

# Printing the global variable
 print("Global variable x:" m)