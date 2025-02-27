# На вход программе подаётся строка текста, в которой буква «h» встречается минимум два раза.
# Напишите программу, которая удаляет из этой строки первое и последнее вхождение буквы «h»,
# а также все символы, находящиеся между ними.

# string = input()
# first_h = string.find('h')
# last_h = string.rfind('h')
# result = string[:first_h] + string[last_h+1:]
# print(result)

#  Коротший варіант

string = input()
print(string[:string.find('h')] + string[string.rfind('h') +1:])
