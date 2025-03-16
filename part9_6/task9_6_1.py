# Используя метод format(), дополните приведённый ниже код так, чтобы он вывел текст:
# In 2010, someone paid 10k Bitcoin for two pizzas.

# was:
# s = 'In {0}, someone paid {1} {2} for two pizzas.'
# print()

year = 2010
price = 10
coin = 'Bitcoin'
s = 'In {0}, someone paid {1}k {2} for two pizzas.'.format(year, price, coin)
print(s)

