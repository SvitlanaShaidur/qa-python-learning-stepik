# Напишите программу, которая считывает натуральное число nи выводит первые n чисел последовательности Фибоначчи

num = int(input())
fib1 = 1
fib2 = 1
for i in range(num):
    print(fib1, end = ' ')
    fib1, fib2 = fib2, fib1 + fib2