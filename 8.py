'''8.Access Modifiers(python)
1. Create a class with PRIVATE fields, private method and a main method. Print the fields 
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.
2. Create a class with PROTECTED fields and methods. Access these fields and methods 
from any other class in the same package. 
Also, Access the PROTECTED fields and methods from child class located in a different 
package
Access the PROTECTED fields and methods from any class in different package
3. Create a class with PUBLIC fields and methods. 
Access the public methods and fields from any class in the same package or different 
packag
Here's an example implementation of access modifiers in Python:

Accessing private fields and methods:'''

class Example:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __private_method(self):
        print("This is a private method")

    def main_method(self):
        print("a: ", self.__a)
        print("b: ", self.__b)
        self.__private_method()

class SubClass(Example):
    def sub_class_method(self):
        # This will give an error because private fields and methods cannot be accessed from outside the class
        # print("a: ", self.__a)
        # print("b: ", self.__b)
        # self.__private_method()
        pass

example = Example(1, 2)
example.main_method()
# Output:
# a: 1
# b: 2
# This is a private method

sub_class = SubClass(3, 4)
sub_class.sub_class_method()
#Accessing protected fields and methods:

# In the same package
class Example:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def _protected_method(self):
        print("This is a protected method")

class AnotherClass:
    def access_protected(self, example):
        print("a: ", example._a)
        print("b: ", example._b)
        example._protected_method()

example = Example(1, 2)
another_class = AnotherClass()
another_class.access_protected(example)
# Output:
# a: 1
# b: 2
# This is a protected method

# In a different package
class ChildClass(Example):
    def access_protected(self):
        print("a: ", self._a)
        print("b: ", self._b)
        self._protected_method()

child_class = ChildClass(3, 4)
child_class.access_protected()
# Output:
# a: 3
# b: 4
# This is a protected method



#Accessing public fields and methods:

class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def public_method(self):
        print("This is a public method")

class AnotherClass:
    def access_public(self, example):
        print("a: ", example.a)
        print("b: ", example.b)
        example.public_method()

class ChildClass:
    def access_public(self, example):
        print("a: ", example.a)
        print("b: ", example.b)
        example.public_method()

example = Example(1, 2)
another_class = AnotherClass()
another_class.access_public(example)
# Output:
# a: 1
# b: 2
# This is a public method

child_class = ChildClass()
child_class.access_public(example)