# Даны два числа: натуральное число n и действительное число a.Напишите программу, которая находит площадь указанного правильного многоугольника.

from math import pow, tan, pi
n = int(input())
a = float(input())
print((n * pow(a, 2)) / (4 * tan( pi / n)))