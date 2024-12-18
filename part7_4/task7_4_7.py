# Напишите программу, которая определяет, какое минимальное количество чеканных монет нужно заплатить ведьмаку

num = int(input())
counter = 0
while num != 0:
    if num >= 25:
        num -= 25
        counter += 1
    elif num >= 10:
        num -= 10
        counter += 1
    elif num >= 5:
        num -= 5
        counter += 1
    elif num >= 1:
        num -= 1
        counter += 1
print(counter)