# Quotes inside quotes have to differ
print('He is called "Beisenbek professor"')

#or using backslash

print("We are the \"green\" team")

# Slicing Strings
a = "Yersultan"
print(a[3:])
print(a[:3])
print(a[3:5])

# Modify Strings
b = " Qanagattandyrylmagandyqtarynyzdan "
print(b.upper())
print(b.lower())
print(b.strip()) #cuts all the whitespaces

# String Concatenation
n = "123 "
i = "kzo "
r = "11"
print(n + i + r)

# F-strings
name = "Yersultan"
age = 18
born = 2006
print(f"My name is {name}, I am {age} years old and I was born in {born}")

#capitalizing the first letter
bro = "friend"
print(bro.capitalize())