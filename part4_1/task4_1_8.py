# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

age = int(input())
if age <= 13:
    print('childhood')
if 14 <= age <= 24:
    print('youth')
if 25 <= age <= 59:
    print('maturity')
if age >= 60:
    print('senility')