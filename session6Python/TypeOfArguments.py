# example 1
def func(i, j):
    print(i, j)

func(10, 20) # positional arguments

func(j = 20, i = 10) # keyword argument

# example 2
# defulat value assigned to positional arguments
def func(i, j = 10):
    print(i, j)

func(100, 200)
func(100)

# keyword arguments
def greetings(name, greentmsg):
    print(greentmsg + "  " + name)

greetings(name = 'Hoai', greentmsg = 'Hello')


# function can return multiple values
def largest(a, b):
    if a > b:
        return a, b
    else:
        return b, a

print(largest(100, 200))