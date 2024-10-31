# Программа должна вывести результат применения операции к введенным числам или соответствующий текст, если операция неверная либо если происходит деление на ноль.

num1, num2 = int(input()), int(input())
str = str(input())
if str == '+':
    print(num1 + num2)
elif str == '-':
    print(num1-num2)
elif str == '*':
    print(num1 * num2)
elif str == '/' and num2 == 0:
    print('На ноль делить нельзя!')
elif str == '/':
    print(num1 / num2)
else:
    print('Неверная операция')