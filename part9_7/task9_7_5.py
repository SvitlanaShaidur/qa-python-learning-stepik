# Модератору Сэму за каждый символ его сообщений в комментариях Тимур платит в 🐝 (пчёлках-coin) по следующему тарифу:
# <код символа в таблице Unicode>×3🐝
# А стоимость всего сообщения складывается из суммы стоимостей всех символов.
# Сэму захотелось подсчитать, сколько 🐝 он зарабатывает за свои ответы в комментариях, и просит вас помочь ему.
# На вход программе подаётся строка текста. Требуется написать программу, которая находит стоимость сообщения Сэма
# в 🐝 и выводит текст в следующем формате:
# Текст сообщения: '<текст сообщения Сэма>'
# Стоимость сообщения: <стоимость сообщения Сэма>🐝
# Формат входных данных
# На вход программе подаётся строка текста – очередной ответ Сэма в комментариях.
#
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.


message = input()
total = 0
for c in message:
    total += ord(c)
cost = total * 3
print("Текст сообщения: '{}'".format(message))
print("Стоимость сообщения: {}🐝".format(cost))