print("this i starting point of program ...")

try:
    print(c)
except:
    print("Exception occured")

print("this is end of the program")

print("this is strating point of program ...")
print("program in progress")
try:
    print(10/0)
except ZeroDivisionError:
    print("program completed...")

# example 3: multiple except blocks - try except else, finally

try:
    num1, num2 = 10, 0
    result = num1/num2
    print("result is ", result)
except ZeroDivisionError:
    print("throw ZeroDivisionError exception")
except SyntaxError:
    print("throw SyntaxError exception")
except:
    print("exception hadled...")
else:
    print("no exceptions occured")
finally:
    print("always execut")

# example 4: raising our own exceptions
def enterage(num):
    if num < 0:
        raise ValueError("Only Integers are allowed")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

enterage(10)
enterage(1)
enterage(-10)

