# Напишите программу, проверяющую корректность email адреса.

email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')