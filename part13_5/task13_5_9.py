# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре»
# и преобразует его в «змеиный регистр».
# Примечание 1. Почитать подробнее о стилях именования можно по ссылке.
# Примечание 2. Приведённый ниже код:
# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))
# должен выводить:
# this_is_camel_cased
# is_prime_number

def convert_to_python_case(text):
    new_text = ''
    for i in text:
        if i.isupper():
            new_text += '_' + i.lower()
        else:
            new_text += i
    return new_text[1:]
txt = input()
print(convert_to_python_case(txt))