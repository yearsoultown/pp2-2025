#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.
#Sets  DO NOT ALLOW DUPLICATES values
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Sets are written with curly brackets. {}

#initializing a set
myset = {15,1,32,1000,100}
print(myset)

#The values (True) and (1) are considered the same value in sets, and are treated as duplicates
#The values (False) and (0) are considered the same value in sets, and are treated as duplicates

"-------------------------------------"

#To determine how many items a set has, use the len() function.
print(len(myset))

#Set items can be of any data type
#A set can contain different data types simultaneously

"-------------------------------------"

#type()
print(type(myset))

#It is also possible to use the set() constructor to make a set.
set1 = set(("apple", "banana", "cherry"))
print(set1)

"-------------------------------------"

#Access Set Items
#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop
for x in set1:
    print(x, end = " ")

print(end = "\n")

for x in set1:
    if x != "apple":
        print(x, end=" ")

print(end = "\n")

print("cherry" in set1)

"-------------------------------------"

#Add Set Items ADD() UPDATE()

#add() method: add one item
set1.add("orange")
print(set1)

#update() method: To add items from another set into the current set
set2 = {"yellow", "oranje", "red"}
set1.update(set2)
print(set1)

list = [1,2,3]
set2.update(list)
print(set2)

"-------------------------------------"

#Remove Set Items
#REMOVE(), or the DISCARD() method: To remove an item in a set
set3 = {"pen", "pinapple", "apple"}
set3.remove("pen") #If the item to remove does not exist, remove() WILL raise an error.
set3.discard("pinapple") #If the item to remove does not exist, discard() will NOT raise an error.
print(set3)

#You can also use the pop() method to remove an item, but this method will remove a random item->
#so you cannot be sure what item that gets removed.
set4 = {"pinapple", "apple"}
set4.pop()
print(set4)

#The clear() method empties the set
set5 = {"pen", "pinapple", "apple"}
set5.clear()
print(set5)

#The del keyword will delete the set completely
del set5

"-------------------------------------"

#Loop Sets

#You can loop through the set items by using a for loop:
for x in myset:
    print(x, end = " ")

"-------------------------------------"

print(end = "\n")

#Join Sets
#The UNION() and UPDATE() methods joins all items from both sets.
set6 = {1,2,3}
set7 = {4,5,6}
set8 = set6.union(set7)
print(set8)

#You can use the (|) operator instead of the union() method, and you will get the same result.
set9 = set6 | set7
print(set9)

#Join Multiple Sets
set10 = {"one", "two", "three"}
set11 = set6.union(set7, set10)
print(set11)

set12 = set6 | set7 | set10
print(set12)

#The  (|) operator only allows you to join sets with sets
#The union() method allows you to join a set with other data types, like lists or tuples.
set13 = {10,11,12}
tup = (13,)
set14 = set13.union(tup)
print(set14)

set15 = {1,2,3}
set15.update(set13)
print(set15)

#Both union() and update() will exclude any duplicate items.

#The intersection() method will return a new set, that only contains the items that are present in both sets.
set16 = {1,2,3}
set17 = {3,4,5}
print(set17.intersection(set16))

#You can use the & operator instead of the intersection() method, and you will get the same result.
set18 = set16 & set17
print(set18)

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set19 = {1,2,3}
set20 = {1,3,4}
set20.intersection_update(set19)
print(set20)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set21 = {1,2,3}
set22 = {1,3,4}
set23 = set21.difference(set22)
set24 = set22.difference(set21)
print(set23)
print(set24)

#You can use the - operator instead of the difference() method, and you will get the same result.
set25 = set22 - set21
print(set25)

#Use the difference_update() method to keep the items that are not present in both sets:
set26 = {10,11,12,13}
set27 = {11,12,13,14}
set26.difference_update(set27)
print(set26)

#The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set28 = {10,11,12,13}
set29 = {11,12,13,14}
set30 = set28.symmetric_difference(set29)
print(set30)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set31 = set28 ^ set29
print(set31)

#The symmetric_difference_update() method will also keep all but the duplicates->
#->but it will change the original set instead of returning a new set.
set32 = {10,11,12,13}
set33 = {11,12,13,14}
set32.symmetric_difference_update(set33)
print(set32)

"-------------------------------------"

#isdisjoint()
set34 = {1,2,3}
set35 = {4,5,6}
x = set34.isdisjoint(set35)
print(x)

set36 = {1,2,3,4,5,6,7,8,9,0}
set37 = {1,2,3,4}
print(set37.issubset(set36))
print(set36.issuperset(set37))

