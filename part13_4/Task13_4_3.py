# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую
# список всех делителей данного числа.
# объявление функции
# def get_factors(num):
    #pass
# считываем данные
#n = int(input())
# вызываем функцию
#print(get_factors(n))

def get_factors(num):
    dividers  = [i for i in range(1, num +1) if num % i == 0]
    return dividers
n = int(input())
print(get_factors(n))