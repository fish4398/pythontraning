# create string varaible

# way of creating string variables
s = "welcome"
s = 'wl'
s = str('welcome')

str = "hoai"
print(str + " beautifull girl")
print(str * 2)

# slicing
str = "welcome"
print(str[1: 3])
print(str[:6])
print(str[2:]) #lcome

print(max("abc"))
print(min("abc"))
print(len("welcome"))

# in, not in operators - return true/false
s = "welcome"
print("come" in s) #true
print("lom" in s) #False
print("come" not in s) #False
print("lom" not in s) #true

# testing strings True/False
s = "welcome to python"

# check special character
print(s.isalnum()) # false

# check all the character is on the ASCII charactors
print("Welcome".isalpha()) #true

# check string just have number
print("2921".isdigit()) #true
print("first Number".isidentifier()) #false
print(s.lower()) #true
print("WELCOME".isupper()) #true
print(" ".isspace()) #true

# searching for substrings
s = "welcome to python automation"
print(s.endswith("thon")) #true

print(s.startswith("good")) #false

print(s.find("come")) # 3

print(s.find("become")) # -1 not found

print(s.count("o")) # 3 returns number of occurrences of substrings

# converting  String
s = "String in PYTHON"
s1 = s.capitalize()
print(s1)
s2 = s.title()
print(s2) #String in PYTHON

s3 = s.lower()

s4 = s.upper()

s5 = s.swapcase()

s6 = s.replace("in", "on")