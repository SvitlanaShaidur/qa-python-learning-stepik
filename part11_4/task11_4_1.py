# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

new_list = []
for num in numbers:
    new_list.append(num ** 2)
print(sum(new_list))