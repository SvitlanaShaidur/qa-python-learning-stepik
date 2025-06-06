# Все книги должны быть обязательно отсортированы по возрастанию:
# сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям. Напишите программу, которая проверяет,
# верно ли отсортированы книги.
# На вход вашей программе поступает число n, а затем – n строк, каждая строка представляет собой книгу в следующем формате:
# <фамилия автора> <инициалы автора>, «<название книги>»
# Программа должна вывести «YES» (без кавычек), если книги отсортированы в соответствии с пожеланиями Душнилы,
# или «NO» (без кавычек) в противном случае.
# Формат входных данных
# На вход программе подаются натуральное число n, а затем – n строк.
# Формат выходных данных
# Программа должна вывести «YES» (без кавычек) или «NO» (без кавычек) в соответствии с условием задачи.
# Примечание 1. Обратите внимание, что Душнила игнорирует инициалы автора при сортировке книг.
# Примечание 2. Гарантируется, что книги в наборе не повторяются.
# Примечание 3. Гарантируется, что фамилия автора состоит из одного слова.

num = int(input())
answer = 'YES'
book1 = input()
author = book1[:book1.find(' ')]
book_name = book1[book1.find('«') + 1: book1.rfind('»')]
first_book = author + book_name
for i in range(num -1):
    book2 = input()
    author = book2[:book2.find(' ')]
    book_name = book2[book2.find('«') + 1: book2.rfind('»')]
    current_book = author + book_name
    if current_book < first_book:
        answer = 'NO'
        break
    first_book = current_book
print(answer)