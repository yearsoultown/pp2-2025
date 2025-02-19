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