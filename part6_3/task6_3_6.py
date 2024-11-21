# Даны три вещественных числа a,b,c. Напишите программу, которая находит вещественные корни квадратного уравнения
# ax**2+bx+c=0
from math import *
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
elif d > 0:
    x1 = (-b - sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    x2 = (-b + sqrt(b ** 2 - (4 * a * c))) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))