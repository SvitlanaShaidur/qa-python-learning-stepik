# Напишите программу, которая определяет наименьшее из четырёх чисел.

d1, d2, d3, d4 = int(input()), int(input()), int(input()), int(input())
if d1 < d2:
    d1d2 = d1
else:
    d1d2 = d2
if d3 < d4:
    d3d4 = d3
else:
    d3d4 = d4
if d1d2 < d3d4:
    print(d1d2)
else:
    print(d3d4)