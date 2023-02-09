'''A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B. 
Create three methods in each class, 2 methods are specific to each class and third 
method (override method) should be in all three Classes A, B and C
Create a class with main method. Create an object for each class A, B and C in main 
method and call every method of each class using its own object/instance.
Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above 
process only for data members'''

# Class A
class A:
    def __init__(self, a):
        self.a = a

    def method_A1(self):
        print("Method A1")

    def method_A2(self):
        print("Method A2")

    def method_A3(self):
        print("Method A3 in Class A")

# Class B
class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def method_B1(self):
        print("Method B1")

    def method_B2(self):
        print("Method B2")

    def method_A3(self):
        print("Method A3 in Class B")

# Class C
class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def method_C1(self):
        print("Method C1")

    def method_C2(self):
        print("Method C2")

    def method_A3(self):
        print("Method A3 in Class C")

# Main class
class Main:
    def main_method(self):
        # Object of Class A
        a_obj = A(10)
        a_obj.method_A1()
        a_obj.method_A2()
        a_obj.method_A3()
        print()

        # Object of Class B
        b_obj = B(20, 30)
        b_obj.method_A1()
        b_obj.method_A2()
        b_obj.method_B1()
        b_obj.method_B2()
        b_obj.method_A3()
        print()

        # Object of Class C
        c_obj = C(40, 50, 60)
        c_obj.method_A1()
        c_obj.method_A2()
        c_obj.method_C1()
        c_obj.method_C2()
        c_obj.method_A3()
        print()

        # Call overridden method with super class reference
        b_obj.method_A3 = super(B, b_obj).method_A3
        b_obj.method_A3()
        print()

        c_obj.method_A3 = super(C, c_obj).method_A3
        c_obj.method_A3()
        print()

# Main
main_obj = Main()
main_obj.main_method()
