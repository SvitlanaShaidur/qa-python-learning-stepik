# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.

num = int(input())
flag = True
last_digit = num % 10
while num > 0:
    if last_digit > num % 10:
        flag = False
    last_digit = num % 10
    num = num // 10
if flag:
    print("YES")
else:
    print("NO")