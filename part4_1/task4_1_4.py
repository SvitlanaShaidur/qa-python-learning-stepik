# Напишите программу, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет.

age = int(input())
if age >= 18:
    print('Access provided')
else:
    print('Access denied')