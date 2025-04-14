# На вход программе подаются натуральное число n, затем n строк, затем число k – количество поисковых
# запросов, затем k строк – поисковые запросы. Напишите программу, которая выводит все введённые строки,
# в которых встречаются одновременно все поисковые запросы.
# Примечание. Поиск не должен быть чувствителен к регистру символов.

num = int(input())
lines = []
for _ in range(num):
    lines.append(input())

num_query = int(input())
lines_query = []
for _ in range(num_query):
    lines_query.append(input().lower())

for line in lines:
    line_lower = line.lower()
    for q in lines_query:
        if q not in line_lower:
            break
    else:
         print(line)