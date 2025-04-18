# Дополните приведённый ниже код, чтобы он:
#
# Заменил второй (по порядку) элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый (по порядку) элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список с помощью функции print()
# Примечание. Под удвоением списка мы понимаем добавление к исходному списку всех его элементов,
# сохраняя порядок. Например, при удвоении списка ['py', 'gen'] мы получаем список ['py', 'gen', 'py', 'gen'].

numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers += [4,5,6]
del numbers[0]
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)