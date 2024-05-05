# Напишите функцию get_mo в параметрах функции st_frequent_word, которая на вход принимает текст
# (только английские слова и пробелы), и возвращает самое часто встречающееся слово.
# Если таких слов несколько - верните любое.

def get_mo(text):
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    most_common_word = max(word_counts, key=word_counts.get)
    return most_common_word


print(get_mo("Hello teachmeskills nice nice nice nice to to to to meet u"))