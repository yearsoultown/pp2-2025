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