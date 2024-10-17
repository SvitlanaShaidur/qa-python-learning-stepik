# Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят»
pass1, pass2 = input(), input()
if pass1 == pass2:
    print("Password accepted")
else:
    print("Password not accepted")