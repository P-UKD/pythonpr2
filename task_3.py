angle_1 = float(input())
angle_2 = float(input())
angle_3 = 180 - angle_1 - angle_2

if angle_1 + angle_2 + angle_3 == 180:
    if angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print("Трикутник існує і є прямокутним")
    else:
        print("Трикутник існує але не є прямокутним")
else:
    print("Такий трикутник не існує")