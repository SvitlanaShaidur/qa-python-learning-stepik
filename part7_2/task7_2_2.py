# Даны два целых числа m и n. Напишите программу, которая выводит все целые числа от m до n включительно в порядке возрастания, если m<n, или в порядке убывания в противном случае.

m, n = int(input()), int(input())
for i in range(m, n + 1) or range(m, n - 1, -1):
    print(i)