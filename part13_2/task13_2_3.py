# Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит
# на печать сумму его цифр.
# объявление функции
# def print_digit_sum(num):
#     pass
# считываем данные
# n = int(input())
# вызываем функцию
# print_digit_sum(n)

def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))
n = int(input())
print_digit_sum(n)