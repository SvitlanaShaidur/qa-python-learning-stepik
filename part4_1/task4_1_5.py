# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами
num1, num2, num3 = int(input()), int(input()),int(input())
if (num2 - num1) + num2 == num3:
    print('YES')
else:
    print('NO')
