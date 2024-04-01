x = int(input())
y = int(input())

if x != y:
    x1 = (x + y) / 2 if x < y else x * y * 2
    y1 = (x + y) / 2 if y < x else x * y * 2
    print(x1, y1)
else:
    print("Числа не повинні бути рівні одне одному")
