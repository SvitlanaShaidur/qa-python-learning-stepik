# На вход программе подаётся одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв и выводит текст в следующем формате:
# Количество гласных букв равно <кол-во гласных букв>
# Количество согласных букв равно <кол-во согласных букв>

s = input().lower()
glas = 0
soglas = 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюе':
        glas += 1
    elif s[i] in 'бвгджзйклмнпрстфхцчшщ':
        soglas += 1
print("Количество гласных букв равно", glas)
print("Количество согласных букв равно", soglas)