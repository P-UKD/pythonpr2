x = int(input())
y = int(input())

if x != y:
    x = (x + y) / 2 if x < y else x * y * 2
    y = (x + y) / 2 if y < x else x * y * 2
    print(x, y)
else:
    print("Числа не повинні бути рівні одне одному")
