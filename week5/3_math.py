import math

#1st task
degree = int(input())
radian = degree*(math.pi/180)
print(f"{degree} degree in radian: {radian}")

#2nd task
base1 = int(input())
base2 = int(input())
height = int(input())
area = ((base1+base2)/2) * height
print(f"Area of the trapezoid: {area}")

#3rd task
sides = int(input())
length = int(input())
area = (sides*(length**2))/(4 * math.tan(math.pi / sides))
area = round(area, 2)
print(f"the area of the regular polygon is: {area}")

#4th task
uzyndyq = float(input())
tiktuzu = float(input())
parallelogram = uzyndyq * tiktuzu

print(f"the length of parallelogram is: {parallelogram}")