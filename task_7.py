numbers = [int(input()) for _ in range(3)]
print(sum(x < 0 for x in numbers))
