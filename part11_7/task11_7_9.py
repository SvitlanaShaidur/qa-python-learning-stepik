# На вход программе подаётся строка текста, содержащая целые числа. Напишите программу,
# использующую списочное выражение, которая выведет квадраты чётных чисел, кроме тех квадратов,
# которые оканчиваются на цифру 4.
# Примечание. Программу можно написать в одну строку кода.

print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2  % 10 != 4])