numbers = [float(input()) for _ in range(3)]
print(sum(x.is_integer() for x in numbers))
