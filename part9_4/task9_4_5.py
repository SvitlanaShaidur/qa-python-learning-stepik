# На вход программе подаётся строка текста. Напишите программу, которая проверяет, что строка заканчивается подстрокой .com или .ru.

string = input()
if string.endswith('.com') or string.endswith('.ru'):
    print('YES')
else:
    print('NO')
