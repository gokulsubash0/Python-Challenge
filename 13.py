'''13.Method Overloading
1. Write two methods with the same name but different number of parameters of same type 
and call the methods 
2. Write two methods with the same name but different number of parameters of different 
data type and call the methods 
3. Write two methods with the same name and same number of parameters of same type
and call the methods'''

class Overloading:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

# Main class
if __name__ == "__main__":
    obj = Overloading()
    print("Result 1:", obj.add(1, 2))
    print("Result 2:", obj.add(1, 2, 3))





class Overloading:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c

# Main class
if __name__ == "__main__":
    obj = Overloading()
    print("Result 1:", obj.add(1, 2))
    print("Result 2:", obj.add(1, 2, 3))




class Overloading:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b):
        return a + b

# Main class
if __name__ == "__main__":
    obj = Overloading()
    print("Result:", obj.add(1, 2))

#In Python, method overloading is not possible because Python is dynamically typed and method overloading is not supported by dynamically typed languages. However, the above programs show how to simulate method overloading by using the same method name but with different parameters, either with different number of parameters or different data types, and calling the methods from a main class.