# Дано нечётное натуральное число n. Напишите программу, которая печатает равнобедренный звёздный треугольник с основанием, равным n

n = int(input())
for i in range(1, n // 2 + 2):
    print('*' * i)
for j in range(n // 2, 0, -1):
        print('*' * j)
print()