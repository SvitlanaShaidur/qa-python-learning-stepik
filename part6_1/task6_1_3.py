# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
num = float(input())
if num == 0:
    print("Обратного числа не существует")
else:
    print(num ** -1)