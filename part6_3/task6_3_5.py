# Напишите программу, которая принимает на вход действительное число x и вычисляет по нему значение: ⌊x⌋+⌈x⌉

from math import ceil, floor
num = float(input())
print(ceil(num) + floor(num))