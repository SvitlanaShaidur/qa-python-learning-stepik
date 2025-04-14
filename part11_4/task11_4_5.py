# На вход программе подаются натуральное число n, затем n строк, затем ещё одна строка –
# поисковый запрос. Напишите программу, которая выводит все введённые строки, в которых
# встречается поисковый запрос.

num = int(input())
lines = []
for i in range(num):
    lines.append(input())
query = input().lower()
for line in lines:
    if query in line.lower():
        print(line)

