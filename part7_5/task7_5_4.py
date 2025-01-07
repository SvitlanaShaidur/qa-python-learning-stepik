# Дано натуральное число. Напишите программу, которая вычисляет:
#
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
total = 0
production = 1
counter = 0
vlast_digit = num % 10
while num != 0:
    last_digit = num % 10
    total += last_digit
    production *= last_digit
    counter += 1
    first_digit = num
    num //= 10
print(total)
print(counter)
print(production)
print(total / counter)
print(first_digit)
print(first_digit + vlast_digit)
