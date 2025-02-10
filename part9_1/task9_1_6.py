# На вход программе подаётся одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.

# s = input()
# summ = 0
# for i in range(0, len(s)):
#    summ += int(s[i])
# print(summ)

string_num = input()
summ = 0
for i in string_num:
    summ += int(i)
print(summ)