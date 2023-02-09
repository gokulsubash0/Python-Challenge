#Define a static variable and access that through a class:


class MyClass:
    static_variable = 0

    @staticmethod
    def access_static_variable():
        return MyClass.static_variable

# Access the static variable through the class
print(MyClass.access_static_variable())




#Define a static variable and access that through an instance:

class MyClass:
    static_variable = 0

    @staticmethod
    def access_static_variable():
        return MyClass.static_variable

# Create an instance of the class
my_instance = MyClass()

# Access the static variable through the instance
print(my_instance.access_static_variable())




#Define a static variable and change within the instance:

class MyClass:
    static_variable = 0

    @staticmethod
    def access_static_variable():
        return MyClass.static_variable

# Create an instance of the class
my_instance = MyClass()

# Change the static variable through the instance
my_instance.static_variable = 10

# Access the updated static variable through the class
print(MyClass.access_static_variable())




#Define a static variable and change within the class:

class MyClass:
    static_variable = 0

    @staticmethod
    def access_static_variable():
        return MyClass.static_variable

    @staticmethod
    def change_static_variable(value):
        MyClass.static_variable = value

# Change the static variable through the class
MyClass.change_static_variable(10)

# Access the updated static variable through the class
print(MyClass.access_static_variable())

'''Define a static variable and access that through a class:
In this example, we define a class MyClass with a static variable static_variable and a static method access_static_variable to access the value of the static variable. The value of the static variable is assigned directly to the class using MyClass.static_variable = 0. To access the value of the static variable, we use MyClass.access_static_variable() method which returns the value of static_variable.

Define a static variable and access that through an instance:
In this example, we create an instance of the class MyClass by calling my_instance = MyClass(). To access the value of the static variable, we use my_instance.access_static_variable() method which returns the value of static_variable.

Define a static variable and change within the instance:
In this example, we change the value of the static variable by using my_instance.static_variable = 10. The static variable is updated and accessible from both the class and its instances.

Define a static variable and change within the class:
In this example, we add a static method change_static_variable to change the value of the static variable. We use MyClass.change_static_variable(10) to change the value of static_variable and MyClass.access_static_variable() to access the updated value of static_variable. The updated value of the static variable is accessible from both the class and its instances.'''