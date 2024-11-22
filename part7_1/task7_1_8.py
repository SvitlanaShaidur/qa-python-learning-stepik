# Напишите программу, которая предсказывает размер популяции организмов с  1-го по n-й день (включительно). Программа должна выводить номер дня, а затем через пробел размер популяции в этот день.


creature, proc, days = int(input()), int(input()), int(input())
for i in range(days):
    population = creature * ((proc / 100) + 1) ** i
    print(i + 1, population)


