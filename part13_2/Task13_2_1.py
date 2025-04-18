# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.
# Примечание. Гарантируется, что основание треугольника – нечётное число.
# # объявление функции
# def draw_triangle(fill, base):
#     pass
# считываем данные
# fill = input()
# base = int(input())
# вызываем функцию
# draw_triangle(fill, base)

def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)
fill = input()
base = int(input())
draw_triangle(fill, base)