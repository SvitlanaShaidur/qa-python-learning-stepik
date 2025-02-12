# На вход программе подаётся строка текста. Напишите программу, которая разрежет её на две равные части, переставит их местами и выведет на экран.
# Если длина строки нечётная, то длина первой части должна быть на один символ больше.

string = input()
part1 = len(string) // 2
part2 = len(string) - part1
if part2 > part1:
    print(string[part2:] + string[:part2])
else:
    print(string[part1:] + string[:part1])