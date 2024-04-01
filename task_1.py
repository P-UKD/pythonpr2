numbers = [float(input()) for _ in range(3)]
results = [x ** 2 if x >= 0 else x ** 4 for x in numbers]
print(results)
