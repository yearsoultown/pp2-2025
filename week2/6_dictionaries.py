#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, CHANGEABLE and DO NOT ALLOW duplicates.
mydict = {
    "name": "Yersultan",
    "age": 18,
    "city": "Almaty"
}
print(mydict)
print(mydict["name"])

#length
print(len(mydict))

#The values in dictionary items can be of any data type:
dict1 = {
    "Name": "Dinara",
    "age": 40,
    "children": ["Yerzhas", "Yersultan", "Aisha", "Baqdaulet"]
}
print(dict1["children"])

# type() = <class 'dict'>

#It is also possible to use the dict() constructor to make a dictionary.
dict2 = dict(name = "Yerzhas", age = 19, university = "Narxoz")
print(dict2["university"])
y = dict2.values()
x = dict2.items()
print(x)
print(y)

if "university" in dict2:
    print("Yes, it is")
else:
    print("No, it is not")

"-------------------------------------"

#change value
dict2["university"] = "AUES"
print(y)

dict2.update({"age": 20})
print(y)

"-------------------------------------"

#Adding items
dict2["hobby"] = "playing dota"

dict2.update({"gym": "saryarqa"})
print(x)

#Removing items
dict2.pop("gym")
print(dict2)

dict2.popitem() #removes the last element inserted
print(dict2)

del dict2["university"]
print(dict2)

dict2.clear()
print(dict2)

#Loop

dict3 = {
    "name": "Aliya",
    "age": 18,
    "uni": "KBTU"
}

for l in dict3:
    print(l,end = " ")

print(end = "\n")

for i in dict3:
    print(dict3[i],end = " ")

print(end = "\n")

for u in dict3.values():
    print(u, end = " ")

print(end = "\n")

for u in dict3.keys():
    print(u,end = " ")
print(end = "\n")

for x, y in dict3.items():
    print(x,":", y)

"-------------------------------"

#Copy a Dictionary
dict4 = dict3.copy()
print(dict4)

dict5 = dict(dict4)
print(dict5)

#Nested dictionaries
myparents = {
    "Mother" : {
        "Name": "Dinara",
        "Surname":"Stampulova",
        "Age":40
    },

    "Father": {
        "Name": "Olzhas",
        "Surname":"Makishev",
        "Age":41
    }
}

print(myparents)

child1 = {
    "name":"Yerzhas"
}
child2= {
    "name":"Yersultan"
}
child3= {
    "name":"Aisha"
}
child4= {
    "name":"Baqdaulet"
}

children = {
    "child1":child1,
    "child2":child2,
    "child3":child3,
    "child4":child4
}

print(children)

#Access Items in Nested Dictionaries
#print(myfamily["child2"]["name"])
print(myparents["Mother"]["Name"])
print(children["child3"]["name"])

for x, obj in children.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])