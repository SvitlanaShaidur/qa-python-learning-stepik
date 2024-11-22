# Дано предложение и количество раз, сколько его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.

sentence = str(input())
iteration = int(input())
for _ in range(iteration):
    print(sentence)