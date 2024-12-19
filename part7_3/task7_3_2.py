# Напишите программу, которая подсчитывает сумму введенных чисел (не включая само число n)

n = int(input())
total = 0
for _ in range(n):
    num = int(input())
    total = total + num
print(total)