# На вход программе подаётся число n(n>1). Напишите программу, которая выводит его наименьший отличный от 1 делитель.

num = int(input())
for i in range(2, num + 1):
   if num % i == 0:
      break
print(i)