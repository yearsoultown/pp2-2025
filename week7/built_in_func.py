"""
all()
any()	
ascii()
bin()
bytearray()	
bytes()	
callable()	
chr()
classmethod()	- Converts a method into a class method
compile()	
complex()	
delattr()	
dir()
divmod()	
enumerate()
eval()	
exec()
filter()	
format()
frozenset()
getattr()	
globals()
hasattr()
hash()	Returns the hash value of a specified object
help()	Executes the built-in help system
hex()
isinstance()
issubclass()	
iter()
locals()	
map()	
memoryview()	
next()
object()	
oct()
ord()	
property()	Gets, sets, deletes a property
repr()	Returns a readable version of an object
setattr()	
slice()
staticmethod() Converts a method into a static method
sum()	
super()	
vars()	
zip()
"""

#The all() function returns True if all items in an iterable are true, otherwise it returns False. -> all(iterable)
mylist = [True, True, True]
x = all(mylist)
print(x)

#The any() function returns True if any item in an iterable are true, otherwise it returns False.
y = any(mylist)
print(y)

#The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
#The ascii() function will replace any non-ascii characters with escape characters:

asciii = "My names is Yersultán 18"
print(ascii(asciii))

#The bin() function returns the binary version of a specified integer.
print(bin(23))

#The bytearray() function returns a bytearray object.
print(bytearray(4))

#The bytes() function returns a bytes object.
print(bytes(4))

#The callable() function returns True if the specified object is callable, otherwise it returns False. A normal variable is not callable
def callme(callmee):
    print(callmee)
    
callmee = "Yersultan"
print(callable(callme))

#The chr() function returns the character that represents the specified unicode.
print(chr(97))

#The compile() function returns the specified source as a code object, ready to be executed.
com = compile('print(55)', 'test', 'eval')
exec(com)

#The complex() function returns a complex number by specifying a real number and an imaginary number.
compl = complex(3, 4)
print(compl)

#1st
import math
lst = [12, 2, 4, 3, 6]
print("Product of the list: ", math.prod(lst))

#2nd
s = input()
upp = sum(map(str.isupper, s))
low = sum(map(str.islower, s))
print("Uppercase: ", upp)
print("Lowercase: ", low)

#3rd
def is_palindrome(s):
    if list(s) == list(reversed(s)):
        return True
    return False

s = input()
print(is_palindrome(s))

#4th
import time

def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

num = 25100
delay = 2123
result = delayed_sqrt(num, delay)
print(f"Square root of {num} after {delay} miliseconds is {result}")

#5th
def check(a):
    return all(a)

a = (True, True, True)
print(check(a))
b = (True, False, True)
print(check(b))