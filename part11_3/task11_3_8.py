# На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.

num = int(input())
words = []
letter = ''
for i in range(num):
    words.append(input())
k = int(input())
for j in words:
    if k <= len(j):
        letter += j[k-1]
print(letter)
