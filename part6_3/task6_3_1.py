# Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

from math import sqrt
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x = (x1 - x2) ** 2
y = (y1 - y2) ** 2
print(sqrt(x + y))