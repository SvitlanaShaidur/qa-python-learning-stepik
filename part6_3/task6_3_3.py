# Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.

from math import sqrt
a, b = float(input()), float(input())
print((a + b) / 2)
print(sqrt(a * b))
print((2 * (a * b)) / (a + b))
print(sqrt ((pow(a, 2) + pow(b, 2)) / 2))