# Нужно написать программу, которая подсчитывает и выводит сумму всех чётных чисел последовательности. Если таких чисел нет, программа должна вывести 0

s = 0
for i in range(1, 8):
    n = int(input())
    if n % 2 == 0:
        s += n
if s > 0:
    print(s)
else:
    print('0')