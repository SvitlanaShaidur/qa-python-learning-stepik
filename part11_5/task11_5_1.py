# На вход программе подаётся строка текста. Напишите программу, которая выводит слова введённой строки в столбик.

s = input()
words = s.split()
print(*words, sep='\n')