# Напишите программу, которая считывает названия двух основных цветов для смешивания.

color1, color2 = str(input()), str(input())
if color1 == "красный" and color2 == "синий" or color2 == "красный" and color1 == "синий":
    print("фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color2 == "красный" and color1 == "желтый":
    print("оранжевый")
elif color1 == "синий" and color2 == "желтый" or color2 == "синий" and color1 == "желтый":
    print("зеленый")
elif color1 == color2 and (color1 == "красный" or color1 == "синий" or color1 == "желтый"):
    print(color1)
else:
    print("ошибка цвета")
