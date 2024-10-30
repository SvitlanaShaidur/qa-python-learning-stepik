# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от  0 до 36

num = int(input())
if 36 >= num >= 0:
    if num == 0:
        print("green")
    elif num % 2 == 0 and (1 <= num <= 10):
        print("black")
    elif num % 2 != 0 and (1 <= num <= 10):
        print("red")
    elif num % 2 == 0 and (11 <= num <= 18):
        print("red")
    elif num % 2 != 0 and (11 <= num <= 18):
        print("black")
    elif num % 2 == 0 and (19 <= num <= 28):
        print("black")
    elif num % 2 != 0 and (19 <= num <= 28):
        print("red")
    elif num % 2 == 0 and (29 <= num <= 36):
        print("red")
    elif num % 2 != 0 and (29 <= num <= 36):
        print("black")
else:
    print("input error")