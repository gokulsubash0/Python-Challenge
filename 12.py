'''12.Constructors
1. Write a class with a default constructor, one argument constructor and two argument 
constructors. Instantiate the class to call all the constructors of that class from a main 
class
2. Call the constructors(both default and argument constructors) of super class from a child 
class
3. Apply private, public, protected and default access modifiers to the constructor
4. Write a program which illustrates the concept of attributes of a constructor.

Here is a sample program that demonstrates the different operations you asked for:'''

# Class with multiple constructors
class Person:
    def __init__(self, name = None, age = None):
        self.__name = name
        self.__age = age

    def __init__(self, name):
        self.__name = name
        self.__age = None

    def __init__(self):
        self.__name = None
        self.__age = None

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

# Main class
if __name__ == "__main__":
    p1 = Person()
    p2 = Person("John")
    p3 = Person("Jane", 30)

    print("Person 1:", p1.get_name(), p1.get_age())
    print("Person 2:", p2.get_name(), p2.get_age())
    print("Person 3:", p3.get_name(), p3.get_age())

# Child class calling super class constructors
class Student(Person):
    def __init__(self, name = None, age = None, id = None):
        Person.__init__(self, name, age)
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

# Main class
if __name__ == "__main__":
    s1 = Student()
    s2 = Student("John")
    s3 = Student("Jane", 30, 123)

    print("Student 1:", s1.get_name(), s1.get_age(), s1.get_id())
    print("Student 2:", s2.get_name(), s2.get_age(), s2.get_id())
    print("Student 3:", s3.get_name(), s3.get_age(), s3.get_id())

# Access modifiers for constructor
class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

# Main class
if __name__ == "__main__":
    e = Employee("John", 30, 5000)
    print("Employee:", e.get_name(), e.get_age(), e.get_salary())

# Attributes of a constructor
class Shape:
    def __init__(self, sides):
        self.__sides = sides

    def get_sides(self):
        return self.__sides

class Square(Shape):
    def __init__(self, sides, length):
        Shape.__init__(self, sides)
        self.__length = length

    def get_area(self):
     return self.__length * self.__length


if name == "main":
 s = Square(4, 5)
print("Square sides:", s.get_sides())
print("Square area:", s.get_area())



#This program demonstrates creating a class with multiple constructors, calling the super class constructors from a child class, using access modifiers for the constructor, and illustrating the concept of attributes of a constructor.