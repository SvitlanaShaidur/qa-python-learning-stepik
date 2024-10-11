num = int(input())
digit3 = num % 10
digit2 = num // 10 % 10
digit1 = num // 100

print('Sum of digits =', digit1 + digit2 + digit3)
print('Multiplication of digits =', digit1 * digit2 * digit3)