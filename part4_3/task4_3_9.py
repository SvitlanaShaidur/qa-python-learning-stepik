#   На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение.

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if b1 < a2 or b2 < a1:
    print("пустое множество")
elif a1 == a2 and b1 == b2:
    print(a1, b1)
elif b1 == a2:
    print(b1)
elif b2 == a1:
    print(b2)
elif a1 < a2 < b1 and b2 > b1:
    print(a2, b1)
elif a2 < a1 < b2 and b1 > b2:
    print(a1, b2)
elif a2 < b1 < b2 and a2 > a1:
    print(a2, b1)
elif a1 < b2 < b1 and a1 > a2:
    print(a1, b2)
elif a1 < a2 and b2 == b1:
    print(a2, b2)
elif a2 < a1 and b1 == b2:
    print(a1, b1)
elif a1 < a2 and b1 > b2:
    print(a2, b2)
elif a2 < a1 and b2 > b1:
    print(a1, b1)
elif b1 < b2 and a1 == a2:
    print(a1, b1)
elif b2 < b1 and a1 == a2:
    print(a2, b2)