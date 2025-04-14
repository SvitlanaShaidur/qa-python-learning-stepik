# На вход программе подается натуральное число n, где n≥2. Затем поступают n целых чисел. Напишите программу,
# которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).

num = int(input())
all_digits = []
sum_number = []
for i in range(num):
    all_digits.append(int(input()))
for k in range(len(all_digits) - 1):
    sum_number.append(all_digits[k] + all_digits[k + 1])
print(sum_number)
