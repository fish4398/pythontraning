"""
class ---> collection of variable(attributes) and methods (behavior)
a class is blue print
logical entity
does not occupy space in the memory

object ---> object is an instance of class
physical entity
occupy certain amount space in the memory

for one class, we can create multiple ojects
ojects are independent

function vs method
function ---> we can create without class
method ---> creates in side the class

2 types of methods we can define within the class
1) instance method (we can call only through object)
2) static method (we can directly call using class
    annotation @staticmethod

class variable

methor and constructor
method: give any name
        return the values
        method can take arguments/parameters
        we have to use an object to invoke the method

constructor: constructor name is fixed:
            def __init__(self):
constructor will not return any value
constructor can also take arguments/parameters
constructor will be called at the time of object creation itself
"""

# example 1

class MyClass:
    def myfun(self):
        pass
    def display(self, name):
        print("john")

# create object
mc1 = MyClass()

mc1.myfun()
mc1.display("Hoai")

# example 2
class MyClass:
    def m1(self):
        print("this is instance method")
    @staticmethod
    def m2(self, num):
        print(self,num)

mc = MyClass()
mc.m1()
mc.m2(100, 399)

MyClass.m2(13, 34)

# Example 3
class MyClass:
    a, b = 10, 20 # class variables
    def add(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a * self.b)

mc = MyClass()
mc.add() #30
mc.mul() # 200

# example 4
i, j = 15, 25 # global variable
class MyClass:
    a, b = 10, 20 # class variables
    def add(self, x, y):
        print(x + y) # local variables
        print(self.a + self.b) # a, b are class variables
        print(i + j)  # i, j are global variable

mc = MyClass()
mc.add(100, 200)

# example 5
a, b = 15, 25 # global variable
class MyClass:
    a, b = 10, 20 # class variables
    def add(self, a, b):
        print(a + b) # local variables
        print(self.a + self.b) # a, b are class variables
        print(globals()['a'] + globals()['b'])  # global variable

mc = MyClass()
mc.add(100, 200)

# example 6
# once class can have multiple ojects
class MyClass:
    def display(self, name):
        print("this is display methor ... ")
        print(name)

obj1 = MyClass()
obj1.display("hoai")

obj1 = MyClass()
obj1.display("scott")

# example 7 constructor example
class MyClass:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("Hello")
    def m2(self, x, y):
        print(x + y)

mc = MyClass() # invke constructor automatically

mc.m1() # method we have call explicitely by using object


# example 8
class MyClass:
    name = "John"
    def __init__(self, name): # constructor expecting on argument
        print(name)
        print(self.name)

mc = MyClass("David") # passing parameter to thr con tructor


# example 9
# reg: emp
# constructor : eid, ename, sal
# display(): print eid, ename and sal

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def display(self):
        print(self.eid, self.ename, self.sal)

e1 = Emp(101, "john", 50000)
e1.display()

# example 10
# reg: emp
# constructor : eid, ename, sal
# display(): print eid, ename and sal

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal
    def __str__(self): # just return string value
        print(self.ename)

e1 = Emp(101, "john", 50000)
print(e1)
