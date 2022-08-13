# create dictionary
mydic = {101: "x", 102: "y", 103: "z"}
print(mydic)

# access items from dictionary
mydic = {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
print(mydic["brand"])
print(mydic["model"])

# using get()
x = mydic.get("brand")
print(x)

# change value in dictionary
print(mydic)
mydic["year"] = 2020
print(mydic)

# reading items from dictionary using loop
for i in mydic:
    print(i)    # print only keys from dictionary

for i in mydic:
    print(mydic[i])

for i in mydic.values():
    print(i)

for x, y in mydic.items():
    print(x, y)       # print keys along with the value

# check key is exists in dictionary or not
if  "model1" in mydic:
    print("exists")
else:
    print("not exists")

print(len(mydic))

# adding items to dictionary
mydic["color"] = "red"
print(mydic)

# remove item from dictionary pop(), del()
mydic.pop("year")
print(mydic)

del mydic["color"]
print(mydic)

mydic.clear()
print(mydic)

# copying dictionary
mydic1= {
    "brand": "Hyudai",
    "model": "i10",
    "year": 2021
}
# using copy function
mydic2 = mydic1.copy()
print(mydic2)
# withot using copy()
mydic3 = mydic1
print(mydic3)