# На вход программе подаётся строка текста, содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести изменённую строку.
# Примечание. Используйте подходящие встроенные функции и списочные методы.

# nums = input().split()
# for i in range(len(nums)):
#    nums[i] = int(nums[i])

nums = [int(i) for i in input().split()] 
min_num = nums.index(min(nums))
max_num = nums.index(max(nums))
nums[min_num], nums[max_num] = nums[max_num], nums[min_num]
print(*nums)
