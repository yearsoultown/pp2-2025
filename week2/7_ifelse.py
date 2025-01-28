a = 200
b = 33

#combination of if elif and else
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#one-line if-statement
if a > b: print("a is greater than b")

#Short Hand If ... Else
c = 2
d = 330
print("C") if c > d else print("D")

#Short Hand If ... Elif... Else
e = -330
f = -330
print("E") if e > f else print("=") if e == b else print("F")

# and or not
if a > b and e == f:
  print("true")

#if statements cannot be empty, but if you for some reason have an if->
#statement with no content, put in the pass statement to avoid getting an error.
x = 10
y = 129

if y > x:
  pass