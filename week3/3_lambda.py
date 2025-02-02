#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

x = lambda b: b *100
print(x(2))

y = lambda a,b: a**b
print(y(2,3))

z = lambda a,b,c: a + b + c
print(z(5,15,25))

#lambda inside the function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#myfunc(2) is called, so n = 2.
#The function returns lambda a: a * 2.
#mydoubler now holds this lambda function, meaning mydoubler(a) is equivalent to a * 2
