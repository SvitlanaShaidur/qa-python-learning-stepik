# Определите, через какое время (в часах) старушки встретятся, если расстояние между ними равно S км.
distance, speed1, speed2 = float(input()), float(input()), float(input())
time = distance / (speed1 + speed2)
print(time)