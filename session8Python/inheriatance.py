"""
class
object ---> methods, static methods, constrictors
inheritance ---> types, overriding, super()
polymorphism --->
"""


# example 1
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m2(self):
        print("this is m2 method from class b")

bobj = B()
bobj.m1()
bobj.m2()

# example 2 simple inheritance
class A:
    x, y = 10, 20
    def m1(self):
        print(self.x, self.y)

class B(A):
    a, b = 200, 100
    def m2(self):
        print(self.a - self.b)

simple = B()
simple.m2()
simple.m1()

# example 3: multilever inheritance
class A:
    x, y = 10, 20
    def m1(self):
        print(self.x + self.y)

class B(A):
    a,  b = 200, 100
    def m2(self):
        print(self.a - self.b)

class C(B):
    i,  j = 5, 4
    def m3(self):
        print(self.i * self.j)

cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()

# example 4: heirarchy inheritance
class A:
    x, y = 10, 20
    def m1(self):
        print(self.x + self.y)

class B(A):
    a,  b = 200, 100
    def m2(self):
        print(self.a - self.b)

class C(A):
    i,  j = 5, 4
    def m3(self):
        print(self.i * self.j)

cobj = C()
cobj.m1()
cobj.m3()

simple = B()
simple.m2()
simple.m1()

# example 5: multiple inheritance
class A:
    x, y = 10, 20
    def m1(self):
        print(self.x + self.y)

class B:
    a,  b = 200, 100
    def m2(self):
        print(self.a - self.b)

class C(A, B):
    i,  j = 5, 4
    def m3(self):
        print(self.i * self.j)

cobj = C()
cobj.m1()
cobj.m2()
cobj.m3()

# example 6: calling parent class method using child class(super())
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m1(self):
        print("this is m1 method from class B")
        super().m1()

bobj = B()
bobj.m1()  # this is m1 method from class B
            # this is m1 method from class A

# example 7
class A:
    a, b = 10, 20

class B(A):
    i, j = 100, 200
    def m(self, x, y):
        print(x + y) # local variables
        print(self.i + self.y) # class variables
        print(self.a + self.b) # class variables

bobj = B()
bobj.m(1000, 2000)

# example 8: overriding variables
class Parents:
    name = "Scott"

class Child(Parents):
    name = "John" # overriding the variable value
    def test(self):
        print(super().name)

cobj = Child()
print(cobj.name)    # John
print(cobj.test())  # Scott

# example 9: overriding method
class Bank:
    def rateOfInterest(self):
        return 0

class XBank(Bank):
    def rateOfInterest(self):
        return 10

class YBank(Bank):
    def rateOfInterest(self):
        return 12

objx = XBank()
objx.rateOfInterest() # 10

objx = YBank()
objx.rateOfInterest() # 12

# example 10: overloading (popymorphism)
class Human:
    def sayHello(self, name = None):
        if name is not None:
            print("Hello " + name)
        else:print("Hello")

h = Human()
h.sayHello("Scott")

# example 11: overloading
class Calculation:
    def add(self, a = 0, b = 0, c = 0):
        print(a + b + c)

calobj = Calculation()
calobj.add()
calobj.add(100, 200)
calobj.add(34, 23 ,12)