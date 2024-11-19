# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

city1, city2, city3 = input(), input(), input()
city_len1 = len(city1)
city_len2 = len(city2)
city_len3 = len(city3)
if min(city_len1, city_len2, city_len3) == city_len1:
    print(city1)
elif min(city_len1, city_len2, city_len3) == city_len2:
    print(city2)
elif min(city_len1, city_len2, city_len3) == city_len3:
    print(city3)
if max(city_len1, city_len2, city_len3) == city_len1:
    print(city1)
elif max(city_len1, city_len2, city_len3) == city_len2:
    print(city2)
elif max(city_len1, city_len2, city_len3) == city_len3:
    print(city3)
