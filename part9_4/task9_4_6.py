# На вход программе подаётся строка текста. Напишите программу, которая выводит на экран символ, который появляется наиболее часто.

s = input()
max_count = 0
most_frequent = ''
for i in s:
    count = s.count(i)
    if count >= max_count:
        max_count = count
        most_frequent = i
print(most_frequent)