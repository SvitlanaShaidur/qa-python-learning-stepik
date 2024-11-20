# Вводятся  3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих строк построить арифметическую прогрессию.

string1, string2, string3 = len(input()), len(input()), len(input())
len_max = max(string1, string2, string3)
len_min = min(string1, string2, string3)
len_mid = (string1 + string2 + string3) - len_max - len_min
if len_max - len_mid == len_mid - len_min:
    print("YES")
else:
    print("NO")
