# Напишите программу, которая классифицирует треугольник на основе длин его сторон.

side1, side2, side3 = int(input()), int(input()), int(input())
if side1 == side2 == side3:
    print("Equilateral")
elif side2 == side1 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalelateral")