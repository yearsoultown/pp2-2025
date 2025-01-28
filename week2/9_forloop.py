#Looping through lists
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) #exits after printing banana
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) #exits loop before printing banana (prevents)

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x, end = " ")

print(end="\n")

for x in range(2, 30, 3):
  print(x, end = " ")

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass
for x in [0, 1, 2]:
  pass
