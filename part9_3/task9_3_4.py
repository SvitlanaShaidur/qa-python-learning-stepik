# На вход программе подаётся строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.

string = input()
counter_low = 0
for i in string:
    if i.islower():
        counter_low += 1
print(counter_low)
