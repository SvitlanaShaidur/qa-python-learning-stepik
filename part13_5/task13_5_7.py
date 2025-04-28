# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку основатель BEEGEEK
# фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть чётным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является действительным паролем BEEGEEK банка, или False в противном случае.

def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False

    if not (parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit()):
        return False

    a = int(parts[0])
    b = int(parts[1])
    c = int(parts[2])

    return is_palindrome(a) and is_prime(b) and is_even(c)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_palindrome(number):
    text = str(number)
    return text == text[::-1]

def is_even(number):
    return number % 2 == 0

psw = input()
print(is_valid_password(psw))
