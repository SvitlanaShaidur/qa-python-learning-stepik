# На вход программе подается натуральное число n, а затем  n строк. Напишите программу, которая создает
# список из символов всех строк, а затем выводит его.

num = int(input())
symbols = []
for i in range(num):
    symbols.extend(input())
print(symbols)