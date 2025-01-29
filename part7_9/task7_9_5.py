# Программа должна вывести цифровой корень введённого числа.

num = int(input())
while num > 9:
    suma = 0
    while num != 0:
        suma += num % 10
        num //= 10
    num = suma
print(num)

