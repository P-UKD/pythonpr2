import math

x1 = float(input("A.x: "))
y1 = float(input("A.y: "))

x2 = float(input("B.x: "))
y2 = float(input("В.y: "))

distance_A = math.sqrt(x1**2 + y1**2)
distance_B = math.sqrt(x2**2 + y2**2)

if distance_A < distance_B:
    print("Точка А знаходиться ближче до початку координат.")
elif distance_B < distance_A:
    print("Точка В знаходиться ближче до початку координат.")
else:
    print("Точка А та точка В знаходяться на однаковій відстані до початку координат.")