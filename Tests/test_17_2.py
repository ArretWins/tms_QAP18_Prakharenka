# Написать для 3 и 4 задания в HW 5 тесты (полные покрытие) и 1 и 3 задание в HW 6
# 1 Параметризация
# 2 Фикстуры (для открытия и закрытия файлов) для HW 6
# 3 Использовать mark для разного запуска тестов
# 4* Исправить код оригинального задания так чтобы проходил без ошибок

# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

import pytest
from pytest import mark


def get_longest_word(text):
    all_words = text.split()
    return max(all_words, key=len)


class TestClass2:
    @mark.Hw5_4
    def test_1(self):
        assert get_longest_word('hellooooooooo world') == 'hellooooooooo'

    @mark.Hw5_4
    @mark.parametrize('arg, expected_exception', [
        ('Hello teachmeskills nice to meet u', 'teachmeskills'),
        ('1', '1'),
    ])
    def test_2(self, arg, expected_exception):
        assert get_longest_word(arg) == expected_exception

    @mark.Hw5_4
    @mark.parametrize('arg, expected_exception', [
        (5, AttributeError),
        ('', ValueError),
        ('   ', ValueError), #пробелы
    ])
    def test_3(self, arg, expected_exception):
        with pytest.raises(expected_exception):
            get_longest_word(arg)

    @mark.Hw5_4
    def test_4(self):
        assert get_longest_word('abc def') == 'abc'

    @mark.Hw5_4
    def test_5(self):
        assert get_longest_word('I am learning python!') == 'learning'