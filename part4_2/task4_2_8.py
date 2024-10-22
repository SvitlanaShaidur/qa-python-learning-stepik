# Напишите программу, которая определяет, может ли король попасть с первой клетки на вторую одним ходом.

x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
if (x1 - 1 <= x2 <= x1 + 1) and (y1 - 1 <= y2 <= y1 + 1):
    print("YES")
else:
    print("NO")