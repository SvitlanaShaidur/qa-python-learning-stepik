# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова. Напишите программу, которая принимает
# 4 слова и находит среди них самое тяжёлое слово. Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них.
# Формат входных данных
# На вход программе подаются 4 слова, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести самое тяжёлое слово в строке.

# Перший варіант:
# word1, word2, word3, word4 = input(), input(), input(), input()
# sum1 = 0
# sum2 = 0
# sum3 = 0
# sum4 = 0
# for i in range(len(word1)):
#      sum1 += ord(word1[i])
# for i  in range(len(word2)):
#      sum2 += ord(word2[i])
# for i  in range(len(word3)):
#      sum3 += ord(word3[i])
# for i  in range(len(word4)):
#      sum4 += ord(word4[i])
# max_value = max(sum1, sum2, sum3, sum4)
# if max_value == sum1:
#     print(word1)
# elif max_value == sum2:
#     print(word2)
# elif max_value == sum3:
#     print(word3)
# elif max_value == sum4:
#     print(word4)

# Другий варіант:

words = [input() for _ in range(4)]
max_weight = 0  # початкове значення ваги
heaviest = ""   # змінна для збереження найважчого слова
for word in words: # Проходимось по кожному слову
    weight = 0
    for ch in word:  # Рахуємо "тяжкість" слова як суму Unicode-кодів усіх його символів
        weight += ord(ch)
    if weight > max_weight:
        max_weight = weight
        heaviest = word
print(heaviest)


