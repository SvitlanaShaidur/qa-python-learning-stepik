# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

num = int(input())
vlast_digit = num % 10
flag = True
while num != 0:
    last_digit = num % 10
    if vlast_digit != last_digit:
        flag = False
    num //= 10
if flag:
    print("YES")
else:
    print("NO")

