# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

def get_longest_word(text):
    all_words = text.split()
    return max(all_words, key=len)

print(get_longest_word("Hello teachmeskills nice to meet u"))
