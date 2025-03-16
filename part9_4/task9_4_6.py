# На вход программе подаётся строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

string = input()
max_count = 0
most_frequent = ''
for char in string:
    count = string.count(char)
    if count >= max_count:
        max_count = count
        most_frequent = char
print(most_frequent)