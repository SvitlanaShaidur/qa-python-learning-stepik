# Генератор безопасных паролей
# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.
# Составляющие проекта:
# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for;
# Написание пользовательских функций;
# Работа с модулем random для генерации случайных чисел.

# Подключите модуль random;
# Создайте строковые константы:
# digits: 0123456789;
# lowercase_letters: abcdefghijklmnopqrstuvwxyz;
# uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
# punctuation: !#$%&*+-=?@^_.
# Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

import random
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
chars = ''

# Программа должна запрашивать у пользователя следующую информацию:
# # Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?
# На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы,
# которые могут быть в генерируемом пароле.

qty_pass = int(input('Сколько паролей нужно сгенерировать?'))
len_pass = int(input('Какой длины должен быть пароль? '))
digits_pass = input('Включать ли в пароль цифры от 0 до 9? (да/нет) ').strip().lower()
uppercase_pass = input('Включать ли в пароль прописные буквы? (да/нет)').strip().lower()
lowercase_pass = input('Включать ли в пароль строчные буквы? (да/нет)').strip().lower()
punctuation_pass = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (да/нет)').strip().lower()
exceptions_pass = input('Исключать ли неоднозначные символы "il1Lo0O"? (да/нет)').strip().lower()
if digits_pass == 'да':
    chars += DIGITS
if uppercase_pass == 'да':
    chars += UPPERCASE_LETTERS
if lowercase_pass == 'да':
    chars += LOWERCASE_LETTERS
if punctuation_pass == 'да':
    chars += PUNCTUATION
if exceptions_pass == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

# Напишите функцию generate_password(), которая принимает два аргумента:
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
# Используя цикл for, сгенерируйте необходимое количество паролей.

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password
for _ in range(qty_pass):
    print(generate_password(len_pass, chars))
