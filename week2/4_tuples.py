#A tuple is a collection which is ORDERED and UNCHANGEABLE, ALLOW DUPLICATES
#tuples are ordered, it means that the items have a defined order, and that order will not change.
#tuples are used by () unlike lists with []

#creating tuple
mytuple = ("sister", "brother", "siblings")
print(mytuple)

"-------------------------------------"

#One item tuple, remember the COMMA:
tup1 = ("bro",)
print(type(tup1))

tup2 = ("bro") #not a tuple
print(type(tup2))

#Tuple items can be of any data type
#A tuple can contain different data types simultaneously

#It is also possible to use the tuple() constructor to make a tuple.
tup3 = tuple(("t", "p", "l"))
print(tup3)

"-------------------------------------"

#Access Tuple Items
tup4 = ("a", "b", "c")

#by index
print(tup4[0])
print(tup4[-1])
print(tup4[0:2])

if "a" in tup4:
    print("Yes")
else:
    print("No")

"-------------------------------------"

#You can convert the tuple into a list, change the list, and convert the list back into a tuple. cuz tuple is unchangeable itself
tup5 = ("bro", "sis")
print(tup5)
list1 = list(tup5)
list1[0:2] = ["brother", "sister"]
tup5 = tuple(list1)
print(tup5)

#you can convert it into a list, add your item(s), and convert it back into a tuple.
#You are allowed to add tuples to tuples
tup6 = (1,2,3)
tup7 = (4,5)
tup8 = tup6 + tup7
print(tup8)

"-------------------------------------"

#The del keyword can delete the tuple completely
del tup8

"-------------------------------------"

#Unpacking a Tuple
tup9 = ("apple", "banana", "blueberries")
(red, yellow, blue) = tup9
print(red)
print(blue)
print(yellow)

#If the number of variables is less than the number of values, you can add an * to the variable name and ->
#->the values will be assigned to the variable as a list
tup10 = ("apple", "banana", "cherry", "strawberry", "raspberry")
(zhassyl, sary, *qyzyl) = tup10
print(qyzyl)

#If the asterisk is added to another variable name than the last, Python will assign values to the variable until->
# ->the number of values left matches the number of variables left.

"-------------------------------------"

#Loop Through a Tuple

#You can loop through the tuple items by using a for loop.
tup11 = ("apple", "banana", "cherry")
for x in tup11:
  print(x)

#Use the range() and len() functions to create a suitable iterable.
for x in range(len(tup11)):
  print("hi", end = " ")
  
print(end = "\n")

#You can loop through the tuple items by using a while loop.
i = 0
while i < len(tup11):
   print(tup11[i], end =", ")
   i += 1

"-------------------------------------"

print(end = "\n")

#Join Two Tuples
# +
tup12 = (5,)
tup13 = (4,3,2,1)
tup14 = tup12 + tup13
print(tup14)

# *
tup15 = (1,2,3)
tup16 = tup15 * 2
print(tup16)