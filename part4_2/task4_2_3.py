# Напишите программу, которая принимает целое число x и определяет, принадлежит ли данное число указанным промежуткам.

x = int(input())
if x >= -29 and x <= -2 or x >= 8 and x <= 25:
    print("Belongs to")
else:
    print("Not belongs to")