# На вход программе подаётся одна строка. Напишите программу, которая выводит:
#
# общее количество символов в строке;
# исходную строку, повторённую 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удалённым первым и последним символами.

string = input()
print(len(string))
print(string + string + string)
print(string[0])
print(string[0:3])
print(string[-3:])
print(string[::-1])
print(string[1:-1])