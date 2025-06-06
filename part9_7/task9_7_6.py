# Модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчёлках-coin) по следующему тарифу:
# <код символа в таблице Unicode>×3🐝
# А стоимость всего сообщения складывается из суммы стоимостей всех символов.
# Сэму захотелось подсчитать, сколько 🐝 он зарабатывает за свои ответы в комментариях, и просит вас помочь ему.
# На вход программе подаётся строка текста.
# На этот раз Сэму захотелось схитрить и попробовать увеличить стоимость своего сообщения, заменив в нем некоторые
# буквы: eyopaxcETOPAHXCBM на соответствующие им русские буквы еуорахсЕТОРАНХСВМ.
# На вход программе подаётся строка текста. Требуется написать программу, которая находит стоимость старого и нового
# сообщений Сэма в 🐝 и выводит текст в следующем формате:
# Старая стоимость: <стоимость старого сообщения>🐝
# Новая стоимость: <стоимость нового сообщения>🐝


message = input()
eng_letters = 'eyopaxcETOPAHXCBM'
rus_letters = 'еуорахсЕТОРАНХСВМ'
old_message = message
old_cost = sum(ord(char) for char in old_message) * 3
new_message = ''
for char in message:
    if char in eng_letters:
        index = eng_letters.find(char)
        new_message += rus_letters[index]
    else:
        new_message += char
new_cost = sum(ord(char) for char in new_message) * 3

print(f'Старая стоимость: {old_cost}🐝')
print(f'Новая стоимость: {new_cost}🐝')