#1st task
def square_numbers(nums):
    for num in nums:
        yield num*num

N = int(input())
some_list = []
for i in range(1, N+1):
    some_list.append(i)
    
new_list = list(square_numbers(some_list))
print(new_list)

#2nd task
def even_numbers(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

n = int(input())
one_list = []
for i in range(n+1):
    one_list.append(i)
    
mod_list = list(even_numbers(one_list))
print(",".join(map(str, mod_list)))
    
#3rd task
def threeandfour(nums):
    for num in nums:
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input())
bir_list = []
for i in range(n+1):
    bir_list.append(i)
    
jana_list = list(threeandfour(bir_list))
print(jana_list)

#4th task
def squares(nums):
    for num in nums:
        yield num * num

a = int(input())
b = int(input())
odin_list = []
for i in range(a, b+1):
    odin_list.append(i)
    
noviy_list = list(squares(odin_list))
for i in noviy_list:
    print(i)
    
#5th task
def descending(m):
    i = m
    while m:
        if i < 0:
            break
        yield i
        i -= 1

max = int(input())
another_list = list(descending(max))
print(another_list)

#end