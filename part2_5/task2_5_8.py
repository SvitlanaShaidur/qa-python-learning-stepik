num = int(input())
d3 = num % 10
d2 = num // 10 % 10
d1 = num // 100

print(d1, d2, d3, sep="")
print(d1, d3, d2, sep="")
print(d2, d1, d3, sep="")
print(d2, d3, d1, sep="")
print(d3, d1, d2, sep="")
print(d3, d2, d1, sep="")