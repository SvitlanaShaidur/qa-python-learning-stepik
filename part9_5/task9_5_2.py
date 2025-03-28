# Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером.
# Программа должна вывести «YES» (без кавычек), если искусственный интеллект справился со своей задачей,
# или «NO» (без кавычек) в противном случае. В нашей задаче корректным автомобильным номером будем считать следующие форматы:
# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
# <БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
# где <ЦИФРА> – это любая цифра, а <БУКВА> – это одна из букв кириллицы АВЕКМНОРСТУХ

number_auto = input()
flag = 'NO'
letters = "АВЕКМНОРСТУХ"
if len(number_auto) in (9, 10):
    symbols = number_auto[0] + number_auto[4:6]
    digits = number_auto[1:4] + number_auto[7:]
    underscore = number_auto[6]
    if digits.isdigit() and underscore == '_':
        flag = 'YES'
    for var in symbols:
        if var not in letters:
            flag = 'NO'
            break
print(flag)


