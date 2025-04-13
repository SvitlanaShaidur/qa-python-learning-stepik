# На вход программе подается натуральное число n, а затем n строк. Напишите программу, которая выводит
# только уникальные строки, в том же порядке, в котором они были введены.

num = int(input())
words = []
for i in range(num):
    line = input()
    if line not in words:
        words.append(line)
print(*words, sep='\n')