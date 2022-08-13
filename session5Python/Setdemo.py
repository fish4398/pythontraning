# create set
myset = {"apple", "banana", "cherry"}

# accessing items from set
for i in myset:
    print(i)

# value exists in set or not
print("apple" in myset) #true
print("banana2" in myset)

# adding items to set
# add()    update()
myset.add("orange")

myset.update(["mango", "grapes"])
print(myset)

# find number of item in a set - len()
print(len(myset))

# remove items from set - remove() discard()
myset.remove("banana")
print(myset)

myset.discard("grapes") # discard will not throw any err if the items not exists
print(myset)

# clear all items from set
#myset.clear()
#print(myset) #set

# joining 2 set - union()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# update
set1.update(set2)
print(set1)