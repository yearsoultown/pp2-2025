#lists allow duplicate values
mylist = ["tomato", "potato", "melon", "melon"]
print(mylist)

#length
print(len(mylist))

#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#a list with strings, integers and boolean values
list4 = ["Yersultan", 18, True]

#What is the data type of a list?
list5 = ["apple", "banana", "cherry"]
print(type(list5))

#It is also possible to use the list() constructor when creating a new list.
list6 = list((1,2,3,4,5))
print(list6)

"-------------------------------------"

#Print the second item of mylist
print(mylist[1]) #potato

#Print the (always)last item of the list:
print(mylist[-1])

#Return the third, fourth, and fifth item:
list7= ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list7[2:5])

#This example returns the items from the beginning to, but NOT including, "kiwi":
list8 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list8[:4])
print(list8[2:])
print(list8[-4:-1])
if "apple" in list8:
    print("Yes it is")

#change list items
list8[1] = "watermelon"
list8[2:5] = "one", "two", "three"
list8[5:6] = "ki", "wi"
print(list8)


"-------------------------------------"

#adding items to the list
list9 = ["Yersultan", "Abilseiit", "Torezhan"]
list10 = ["Aliya", "Vika", "Saltanat"]
list9[1:2] = ["Olzhas"]
list9.append("Abilseiit")
list9.insert(1, "Rustem")
list9[4] = "Yersultan"
list9[0] = "Abilseiit"
list9.extend(list10)
print(list9)

#removing items of the list. remove() - deletes the first occurence of item if there are two of them, deletes by the name itself
#pop() - deletes the last item, and by index
#del - deletes the list completely, del[index] - like pop()
#clear() method empties the list. The list still remains, but it has no content.
list11 = ["dont remove this", "remove this one", "remove this one", "a", "b","c"]
list11.remove("remove this one")
list11.pop(0)
del list11[-1]
print(list11)
list11.clear()
print(list11)

"-------------------------------------"

#Loop Through a List
list12 = [1,2,3,4,5,6,7,8,9,0]
for i in list12:
    print(i, end = " ")

print(end = "\n")

for x in range(len(mylist)):
    print(mylist[x], end = " ")

print(end = "\n")

while i < len(mylist):
    print(mylist[i], end=" ")
    i += 1

print(end = "\n")

[print(y, end = " ") for y in mylist]

"-------------------------------------"

#List Comprehension
#adding list elements to another list specified by the rule
list13 = ["Aliya", "Yersultan", "Rustem", "Beibit", "Rico"]
list14 = []
for i in list13:
    if "a" in i:
        list14.append(i)

print(end = "\n")
print(list14)

# newlist = [expression for item in iterable if condition == True]
list15 = [t for t in list13 if "a" not in t]
print(list15)

# !=
list16 = [x for x in list13 if x != "Rico"]
print(list16)

#no condition (if)
list17 = [x for x in list16]
print(list17)

#iterables comprehension
list18 = [x for x in range(10) if x%2==0]
print(list18)

#manipulation before ending
list19 = [x.upper() for x in list13 if x != "Beibit" and x != "Rustem"]
print(list19)

#Set all values in the new list to 'hello'
list20 = ["hello" for x in list13]
print(list20)

#return orange insted of banana
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list21 = [x if x != "banana" else "orange" for x in fruits]
print(list21)

"-------------------------------------"

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default: 
list22 = [20,34,23,11,1]
list22.sort()
print(list22)

#descending order
list22.sort(reverse = True)
print(list22)

#sorts capital letters before lower ones
list23 = ["orange", "yellow", "Red", "Blue"]
list23.sort()
print(list23)

#key
list23.sort(key = str.lower)
print(list23)

"-------------------------------------"

#reverse()
list24 = [1,2,3,4,5]
list24.reverse()
print(list24)


"-------------------------------------"

#Make a copy of a list with the copy() method:
list25 = list24.copy()
print(list25)

#list()
list26 = list(list24)
print(list26)

#slice operator [:]
list27 = list24[:]
print(list27)

#logical
list28 = list24
print(list28)


"-------------------------------------"

#joining the lists
list29 = [1,2,3]
list30 = ["four", "five", "six"]
list31 = list29 + list30
list32 = ["six", "five", "four"]
list33 = [1,2,3]
print(list31)

#append()
for strs in list30:
    list29.append(strs)
print(list29)

#extend()
list33.sort(reverse = True)
list32.extend(list33)
print(list32)

list29.extend(range(10))
print(list29)

"-------------------------------------"

#count
cnt = mylist.count("melon")
print(cnt)

#index
print(list29.index("four"))