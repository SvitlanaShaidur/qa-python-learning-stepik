# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.

speed_zoom, speed_flash = int(input()), int(input())
if speed_zoom > speed_flash:
    print("NO")
elif speed_zoom == speed_flash:
    print("Don't know")
else:
    print("YES")
