num = int(input())
d1 = num //1000 %  10
d2 = num // 100 % 10
d3 = num // 10 % 10
d4 = num % 10

print('The digit in the thousands position is', d1)
print('The digit in the hundreds position is', d2)
print('The digit in the tens position is', d3)
print('The digit in the units position is', d4)
