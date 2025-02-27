# На вход программе подаётся строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.

# string = input()
# counter = 0
# for i in range(10):
#    counter += string.count(str(i))
# print(counter)


# Інше рішення
string = input()
counter = 0
for i in string:
    if i.isdigit():
        counter += 1
print(counter)