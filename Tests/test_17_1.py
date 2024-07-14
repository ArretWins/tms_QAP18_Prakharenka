# Написать для 3 и 4 задания в HW 5 тесты (полные покрытие) и 1 и 3 задание в HW 6
# 1 Параметризация
# 2 Фикстуры (для открытия и закрытия файлов) для HW 6
# 3 Использовать mark для разного запуска тестов
# 4* Исправить код оригинального задания так чтобы проходил без ошибок


# 3 Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.То есть generate_squares(1, 2, 3) -> [1, 4, 9]


import pytest
from pytest import mark


def generate_squares(*args):
    return [i ** 2 for i in args]


class TestClass:
    @mark.Hw5_3
    # @mark.parametrize('args', (1, 2, 3, 4, 5))
    def test_1(self):
        assert generate_squares(1, 2, 3, 4, 5) == [1, 4, 9, 16, 25]

    @mark.Hw5_3
    @mark.parametrize('args, expected_exception', [
                        (('a',), TypeError),
                        (('a', 'b', 'c', 'd'), TypeError),
                      ])
    def test_2(self, args, expected_exception):
        with pytest.raises(expected_exception):
            generate_squares(*args)

    @mark.Hw5_3
    def test_3(self):
        assert generate_squares(-2, 1, 0) == [4, 1, 0]

    @mark.Hw5_3
    def test_4(self):
        assert generate_squares() == []

    @mark.Hw5_3
    def test_5(self):
        assert generate_squares(1.55, 1.01, 2.2332) == [2.4025000000000003, 1.0201, 4.98718224]

    @mark.Hw5_3
    def test_6(self):
        assert generate_squares(10000000000000000000000) == [100000000000000000000000000000000000000000000]
