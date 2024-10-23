# Напишите программу, которая принимает три положительных числа и определяет, существует ли невырожденный треугольник с такими сторонами.

num1, num2, num3 = int(input()), int(input()), int(input())
if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
    print("YES")
else:
    print("NO")
