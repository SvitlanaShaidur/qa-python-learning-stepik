# Программа должна вывести графическое изображение чисел от 1 до n, каждое на отдельной строке.

num = int(input())
counter = 0
for i in range(1, num + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    print(str(i) + '+' * counter)
    counter = 0
