# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

num1, num2, num3 = int(input()), int(input()), int(input())
if num1 > 0:
    num1 = num1
else:
    num1 = 0
if num2 > 0:
    num2 = num2
else:
    num2 = 0
if num3 > 0:
    num3 = num3
else:
    num3 = 0
print(num1 + num2 + num3)