# На вход программе подаётся строка текста, содержащая целые числа.
# Из данной строки формируется список чисел.
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию.

# text = input().split()
# for i in range(len(text)):
#     text[i] = int(text[i])

text = [int(i) for i in input().split()]
text.sort()
print(*text)
text.sort(reverse=True)
print(*text)
