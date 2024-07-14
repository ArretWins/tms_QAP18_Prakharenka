# Написать для 3 и 4 задания в HW 5 тесты (полные покрытие) и 1 и 3 задание в HW 6
# 1 Параметризация
# 2 Фикстуры (для открытия и закрытия файлов) для HW 6
# 3 Использовать mark для разного запуска тестов
# 4* Исправить код оригинального задания так чтобы проходил без ошибок

# Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

import pytest
from pytest import mark, fixture
from pathlib import Path


def sq_files(file, output_file):
    try:
        with open(file, 'r') as f:
            numbers = [float(num) for num in f.readlines()]

            squared_numbers = [num ** 2 for num in numbers]

        with open(output_file, 'w') as nf:
            for squared_num in squared_numbers:
                nf.write(str(squared_num) + '\n')
        print("Done.")
    except Exception as e:
        with open(output_file, 'w') as nf:
            nf.write(str(e))


class TestHw6:
    @fixture
    def create_file(self, tmp_path):
        file_path = tmp_path / "test_file.txt"
        yield file_path

    @fixture
    def output_file(self, tmp_path):
        output_file_path = tmp_path / "output_file.txt"
        yield output_file_path

    @mark.hw6_3
    @mark.parametrize("file_contents, expected_output", [
        ("0\n2\n4\n10\n", ["0.0", "4.0", "16.0", "100.0"]),
        ("1.5\n3.2\n-1\n0\n", ['2.25', '10.240000000000002', '1.0', '0.0']),
        ("", []),
        ("5", ["25.0"]),
        ("a\nb\nc\n", ["could not convert string to float: 'a\\n'"]),
    ])
    def test_sq_files(self, create_file, output_file, file_contents, expected_output):
        create_file.write_text(file_contents)
        sq_files(create_file, output_file)

        # Чтение содержимого выходного файла
        result = output_file.read_text().splitlines()
        assert result == expected_output