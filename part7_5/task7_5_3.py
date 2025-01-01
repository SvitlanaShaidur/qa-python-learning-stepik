# Дано натуральное число  n(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры и выводит текст

num = int(input())
n_max = 0
n_min = 9
while num != 0:
    last_digit = num % 10
    if last_digit > n_max:
        n_max = last_digit
    if last_digit < n_min:
        n_min = last_digit
    num //= 10
print('Максимальная цифра равна', n_max)
print('Минимальная цифра равна', n_min)
