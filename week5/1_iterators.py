#Iterator vs Iterable

#iter() method which is used to get an iterator, next() to iterate the next object:
mytuple = ("qurt", "airan", "mai")
x = iter(mytuple)

print(next(x))
print(next(x))
print(next(x))

mystr = "bruh"
y = iter(mystr)

print(next(y))
print(next(y))
print(next(y))
print(next(y))

