# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля
# password и возвращает значение True, если пароль является надёжным, или False в противном случае.
# Пароль является надёжным, если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

def is_password_good(password):
     if len(password) < 8:
         return False
     with_upper = False
     with_lower = False
     with_digit = False
     for i in password:
         if i.isupper():
             with_upper = True
         elif i.islower():
             with_lower = True
         elif i.isdigit():
             with_digit =  True

     return with_lower and with_digit and with_upper
txt = input()
print(is_password_good(txt))