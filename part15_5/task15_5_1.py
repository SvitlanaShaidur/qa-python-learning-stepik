# На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами
# присутствует один пробел.
# Формат входных данных
# На вход программе подаётся строка текста на английском языке.
# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.
# Примечание. Символы, не являющиеся английскими буквами, не изменяются.


eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt_word(word):
    only_letters = ''.join([char for char in word if char.isalpha()])
    shift = len(only_letters)

    new_word = ''
    for char in word:
        if char in eng_lower:
            new_index = (eng_lower.index(char) + shift) % 26
            new_word += eng_lower[new_index]
        elif char in eng_upper:
            new_index = (eng_upper.index(char) + shift) % 26
            new_word += eng_upper[new_index]
        else:
            new_word += char
    return new_word

text = input()
words = text.split()
encrypted_words = [encrypt_word(word) for word in words]
result = ' '.join(encrypted_words)
print(result)







