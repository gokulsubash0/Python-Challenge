'''9.Abstract Class
1. Create an abstract class with abstract and non-abstract methods.
2. Create a sub class for an abstract class. Create an object in the child class for the 
abstract class and access the non-abstract methods
3. Create an instance for the child class in child class and call abstract methods
4. Create an instance for the child class in child class and call non-abstract methods

Here's an example to demonstrate the creation of an abstract class and its usage:'''


from abc import ABC, abstractmethod

# abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def display(self):
        print("This is a shape.")

# child class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# creating an instance of the child class
sq = Square(5)

# calling non-abstract methods
sq.display()

# calling abstract methods
print("Area of square:", sq.area())


#In this example, the Shape class is an abstract class that defines an abstract method area and a non-abstract method display. The Square class is a child class that inherits from the Shape class and provides an implementation for the area method.

#When you create an instance of the Square class, you can call both the abstract method (area) and the non-abstract method (display) on that instance. The area method returns the area of a square, and the display method prints a message.