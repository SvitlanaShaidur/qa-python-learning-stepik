# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно

num1, num2 = int(input()), int(input())
count = 0
for i in range(num1, num2 + 1):
    for j in range(1, i + 1):
         if i % j == 0:
             count += 1
    if count == 2:
        print(i)
    count = 0

