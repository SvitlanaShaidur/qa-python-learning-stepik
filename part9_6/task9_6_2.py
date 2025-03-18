# Используя f-строку, дополните приведённый ниже код так, чтобы он вывел текст:
#
# In 2010, someone paid 10K Bitcoin for two pizzas.

# was:
# s = 'In {}, someone paid {} {} for two pizzas.'
# print()

year = 2010
price = 10
coin = 'Bitcoin'
s = f'In {year}, someone paid {price}K {coin} for two pizzas.'
print(s)