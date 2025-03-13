# Программа должна принимать на вход натуральное число n, а затем n строк, представляющих тексты комментариев.
# Для каждого комментария ваша программа должна выводить номер этого комментария (начиная с 1),
# затем двоеточие (:), затем через пробел его текст или сообщение «COMMENT SHOULD BE DELETED» (без кавычек),
# если комментарий должен быть удалён

num = int(input())
for i in range(1, num +1):
    comment = input()
    if comment.isspace() or len(comment) == 0:
        print(i, ": COMMENT SHOULD BE DELETED", sep='')
    else:
        print(i, ": ", comment, sep = '')