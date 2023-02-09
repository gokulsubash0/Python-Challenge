'''10.Packages
1. Create a program to create two class.
1.1. Create a constructor and a method for each class
1.2. Create a __init__.py for adding all packages
1.3. Import the respective packages
1.4. Call each class by creating an object to it 
1.5. Create a program by all the above'''

#Here is a sample program that creates two classes, each with a constructor and a method, and demonstrates how to import and use the classes in Python:


# File: my_classes.py

class ClassA:
    def __init__(self, attr1):
        self.attr1 = attr1

    def method_a(self):
        print("ClassA:", self.attr1)

class ClassB:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def method_b(self):
        print("ClassB:", self.attr1, self.attr2)

# File: __init__.py

from .my_classes import ClassA, ClassB

# File: main.py

from my_classes import ClassA, ClassB

obj_a = ClassA("attribute 1")
obj_a.method_a()

obj_b = ClassB("attribute 1", "attribute 2")
obj_b.method_b()
#This program demonstrates how to create two classes, ClassA and ClassB, and how to import them into another file, main.py, using the __init__.py file to add all the packages. The classes are then used by creating objects of each class and calling their respective methods.