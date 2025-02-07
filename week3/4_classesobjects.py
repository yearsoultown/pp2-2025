#Tasks are below(scroll please)
#Create a class named MyClass, with a property named x:

class MyClass:
    x = 5
    
class YourClass:
    d = 10
    
#Now we can use the class named MyClass to create objects

p1 = MyClass()
print(p1.x)

done = YourClass()
print(done.d)

#The __init__() Function
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties
#or other operations that are necessary to do when the object is being created:


#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
p1 = Person("Yersultan", 18)  
print(p1.name)
print(p1.age)

class Person2:
    def __init__(her, name, age):
        her.name = name
        her.age = age
    
p2 = Person2("Aliya", 18)
print(p2.name)

#The __str__() function controls what should be returned when the class object is represented as a string.
#If the __str__() function is not set, the string representation of the object is returned:

#without __str__
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p3 = Person3("John", 36)

print(p1)

#with __str__
class Person4:
    def __init__(him, name, age):
        him.name = name
        him.age = age
    
    def __str__(him):
        return f"{him.name}\n{him.age}"
        
p4 = Person4("Yerzhas", 19)
print(p4)

#Insert a function that prints a greeting, and execute it on the p5 object:
class Person5:
    def __init__(they, name, age):
        they.esim = name
        they.jas = age
        
    def theirname(they):
        print("Hello, my name is - " + they.esim)
        
    def theirage(they):
        print(f"And I am {they.jas} years old")
    
p5 = Person5("Transgender", 29)
p5.theirname()
p5.jas = 40
p5.theirage()
del p5

#The "THEY" parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


#1st task
class strings:
    def __init__(str):
        str.text = ""
        
    def getString(str):
        str.text = input()
        
    def printString(str):
        print(str.text)
         
strr = strings()
strr.getString()
strr.printString()

#2nd task
class shape:
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

square = square(95)
print(f"Площадь квадрата: {square.area()}")

#3rd task
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = rectangle(4, 6)
print(f"Площадь прямоугольника: {rectangle.area()}")

#4th task
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"coordinates of the points: ({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point1.move(4, 6)
point1.show()
print(f"Distance between points: {point1.dist(point2)}")

#5th task
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"top up {amount}. current balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough resources!")
        else:
            self.balance -= amount
            print(f"withdrawal: {amount}. current balance: {self.balance}")

account = Account("Steve", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)

#6th task
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

prime_numbers = list(filter(is_prime, numbers))
print(f"primes: {prime_numbers}")
