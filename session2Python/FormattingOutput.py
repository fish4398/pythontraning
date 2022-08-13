name = "john"
age = 30
sal = 5000.00

name, age, sal = "john", 20, 5000.50

print(name)
print(age)
print(sal)

print(name, age, sal)

# approach3
#print("Name is: %s    Age is: %d     Salary is: $g" %(name, age, sal))

print("Name is: {}    Age is: {}     Salary is: {}" .format(name, age, sal))
