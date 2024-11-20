# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

city1, city2, city3 = input(), input(), input()
print(min(city1, city2, city3, key = len))
print(max(city1, city2, city3, key = len))