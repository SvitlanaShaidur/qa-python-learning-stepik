# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу,
# которая сначала выводит все отрицательные числа, затем нули, а затем все положительные числа,
# каждое на отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

negative = []
positive = []
zero = []
num = int(input())
for _ in range(num):
    digits = int(input())
    if digits < 0:
        negative.append(digits)
    elif digits == 0:
        zero.append(digits)
    else:
        positive.append(digits)
print(*negative, *zero, *positive, sep='\n')

