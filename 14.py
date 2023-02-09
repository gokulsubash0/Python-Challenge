'''14.Exceptions
1. Write a program to generate Arithmetic Exception without exception handling
2. Handle the Arithmetic exception using try-catch block
3. Write a method which throws exception, Call that method in main class without try block
4. Write a program with multiple catch blocks
5. Write a program to throw exception with your own message
6. Write a program to create your own exception
7. Write a program with finally block
8. Write a program to generate Arithmetic Exception
9. Write a program to generate FileNotFoundException
10. Write a program to generate ClassNotFoundException
11. Write a program to generate IOException
12. Write a program to generate NoSuchFieldException

Here is the code for each of the above scenarios:

Generating Arithmetic Exception without exception handling:'''

a = 10
b = 0
c = a / b
print(c)

#Handling the Arithmetic exception using try-catch block:

try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ArithmeticError as e:
    print("Arithmetic Exception:", e)

#Throwing exception in a method and calling it without a try block:

class ThrowException:
    def divide(self, a, b):
        if b == 0:
            raise ArithmeticError("division by zero")
        return a / b

# Main class
if __name__ == "__main__":
    obj = ThrowException()
    print(obj.divide(10, 0))

#Program with multiple catch blocks:

try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ArithmeticError as e:
    print("Arithmetic Exception:", e)
except Exception as e:
    print("Exception:", e)

#Throwing exception with a custom message:

try:
    a = 10
    b = 0
    if b == 0:
        raise Exception("division by zero")
    c = a / b
    print(c)
except Exception as e:
    print("Exception:", e)

#Creating your own exception:

class CustomException(Exception):
    pass

try:
    a = 10
    b = 0
    if b == 0:
        raise CustomException("division by zero")
    c = a / b
    print(c)
except CustomException as e:
    print("Custom Exception:", e)

#Program with finally block:

try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ArithmeticError as e:
    print("Arithmetic Exception:", e)
finally:
    print("Finally block executed")

#Generating Arithmetic Exception:

try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ArithmeticError as e:
    print("Arithmetic Exception:", e)

#Generating FileNotFoundException:

try:
    file = open("file.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundException:", e)

#Generating ClassNotFoundException:

try:
    classObj = globals()["ClassNotFound"]()
except KeyError as e:
    print("ClassNotFoundException:", e)

#Generating IOException:

try:
    file = open("file.txt", "r")
    file.write("Writing to a file")
except IOError as e:
    print("IOException:", e)


#Here is an example to generate a AttributeError in Python, which is equivalent to the NoSuchFieldException in Java:


class Student:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

s = Student(1, "John Doe", "123 Main St")
try:
    email = s.email
except AttributeError as e:
    print("AttributeError:", e)

#The output of the above code will be:
#AttributeError: 'Student' object has no attribute 'email'