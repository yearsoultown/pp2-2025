import re

a = "Valid one"
b = "Invalid one"

#convert a given camel case string to snake case
pattern10 = "([A-Z])"
replacement10 = "_"
string10 = input()
x10 = re.sub(pattern10, lambda y: y.group(1).lower(), string10)
print(x10)