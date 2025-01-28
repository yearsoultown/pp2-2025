#While loop
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")