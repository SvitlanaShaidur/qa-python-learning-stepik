# На вход программе подаётся строка текста и строка-разделитель. Напишите программу,
# которая вставляет указанный разделитель между каждым символом введённой строки текста.

text = input()
divider = input()
print(divider.join(text))
