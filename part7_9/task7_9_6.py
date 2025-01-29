# На вход программе подаётся одно натуральное число. Программа должна вывести значение суммы 1!+2!+3!+…+n!

num = int(input())
summ = 0
multi = 1
for i in range(1, num + 1):
    multi *= i
    summ += multi
print(summ)


# the second variant

from math import factorial
num = int(input())
total = 0
for i in range(1, num + 1):
  total += factorial(i)
print(total)


