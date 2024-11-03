# Напишите программу, которая упорядочивает три числа от большего к меньшему.

num1, num2, num3 = int(input()), int(input()), int(input())
n = max(num1, num2, num3)
n2 = min(num1, num2, num3)
n3 = (num1 + num2 + num3) - n - n2
print(n)
print(n3)
print(n2)
