global_var = 20 # global variable

def func():
    local_var = 10 # local variable
    print(local_var)
    print(global_var)

func()

# example 2
xy = 100

def cool():
    xy = 200
    print(xy)

cool()  # 200

# example 3
xy = 100

def cool():
    global xy
    xy = 200
    print(xy)

cool()  # 200

# example 4
x = 100

def cool():
    global x
    x = 400
    print(x)

cool()    # 500
print(x)   # 500

# example 5
# there is no need to declare global variables outside function
# you can declare them global inside the function

def cool():
    global  x
    x = 200
    print(x)

cool()