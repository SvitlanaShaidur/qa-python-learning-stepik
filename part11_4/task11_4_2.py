# На вход программе подается натуральное число n, а затем n целых чисел. Напишите программу, которая для каждого
# введенного числа x выводит значение функции f(x)=x2+2x+1, каждое на отдельной строке.

num = int(input())
digits = []
for i in range(num):
    digits.append(int(input()))
print(*digits, sep='\n')
print()
for j in digits:
    print(j ** 2 + 2 * j + 1, sep='\n')