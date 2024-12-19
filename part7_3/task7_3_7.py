# На вход программе подается натуральное число n. Напишите программу, которая вычисляет сумму всех его делителей.

num = int(input())
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        total += i
print(total)