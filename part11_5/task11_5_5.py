# На вход программе подаётся строка текста, содержащая 4 целых неотрицательных числа,
# разделённых точкой. Напишите программу, которая определяет, является ли введённая строка текста
# корректным ip-адресом.
# Формат выходных данных
# Программа должна вывести «ДА» (без кавычек), если введённая строка является корректным ip-адресом,
# или «НЕТ» (без кавычек) в противном случае.
#
# Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.

ip = input().split('.')
for i in ip:
    if not 0 <= int(i) <= 255:
        print('НЕТ')
        break
else:
    print('ДА')