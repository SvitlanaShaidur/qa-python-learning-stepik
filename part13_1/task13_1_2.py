# Напишите функцию draw_triangle(), которая выводит звёздный прямоугольный треугольник с катетами, равными 10,
# в соответствии с образцом
# Примечание. Для вывода треугольника используйте цикл for.
# # объявление функции
# def draw_triangle():
#     pass
 # основная программа
# draw_triangle()  # вызов функции

def draw_triangle():
    for i in range(10):
        print('*' * (i + 1))
draw_triangle()
