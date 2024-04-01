a = int(input())
b = int(input())

if a != b:
    m = max([a, b])
    a, b = m, m
else:
    a, b = 0, 0

print(a, b)
