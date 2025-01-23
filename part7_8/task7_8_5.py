# Дано натуральное число n. Напишите программу, которая печатает численный треугольник

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end='')
    print()