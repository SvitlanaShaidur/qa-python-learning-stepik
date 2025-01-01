# Дано натуральное число  n(n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

num = int(input())
while num >= 100:
    num //= 10
second_digit = num % 10
print(second_digit)