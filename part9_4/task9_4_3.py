# Джим Хоппер с помощью радиоприёмника пытается получить сообщение Оди.
# В первой строке подаётся число n – количество сообщений, в последующих строках вводятся сами сообщения.
# Программа должна вывести количество сообщений от Оди.
# Обратите внимание, что в сообщениях Оди вхождения числа 11 должны быть непересекающимися.

num = int(input())
counter = 0
for i in range(num):
    string = input()
    if string.count('11') >= 3:
        counter += 1
print(counter)