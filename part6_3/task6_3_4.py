# Напишите программу, вычисляющую значение тригонометрического выражения
# sinx+cosx+tan**2x по заданному числу градусов x

from math import *
grad = float(input())
rad = radians(grad)
print(sin(rad) + cos(rad) + tan(rad) ** 2)