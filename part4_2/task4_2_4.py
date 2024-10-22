# Назовём число красивым, если оно является четырёхзначным и делится нацело на 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES» (без кавычек), если число является красивым, или «NO» (без кавычек) в противном случае.

num = int(input())
if 1000 <= num <= 9999 and (num % 7 == 0  or num % 17 == 0):
    print("YES")
else:
    print("NO")