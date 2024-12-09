# На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!

count = 1
n = int(input())
for i in range(1, n + 1):
    count *=  i
print(count)
