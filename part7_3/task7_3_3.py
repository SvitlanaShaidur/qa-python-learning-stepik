# На вход программе подается натуральное число n. Напишите программу, которая вычисляет значение выражения

from math import log
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total - log(n))