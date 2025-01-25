#returns True or False
print(9 == 0)
print(9 > 8)
print(9 == 9)
print(9 < 10)

#if-else returns True or False
a = 101
b = 100
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# bool() operator returns True or False (values and variables (list))
print(bool("Hello"))
print(bool(120))

c = "Hello"
d = 19
print(bool(c))
print(bool(d))

bool(["apple", "banana", "orange"])

#Some values are False
bool(False)
bool(0)
bool([])
bool({})
bool(())
bool("")

# isinstance(val, type)
e = 10
print(isinstance(e, int))