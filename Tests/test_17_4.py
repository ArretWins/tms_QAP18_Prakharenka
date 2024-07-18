# Написать для 3 и 4 задания в HW 5 тесты (полные покрытие) и 1 и 3 задание в HW 6
# 1 Параметризация
# 2 Фикстуры (для открытия и закрытия файлов) для HW 6
# 3 Использовать mark для разного запуска тестов
# 4* Исправить код оригинального задания так чтобы проходил без ошибок

# Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

from pytest import mark, fixture


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
        output_file_path.unlink()

    @mark.hw6_3
    @mark.parametrize("file_contents, expected_output", [
        ("0\n2\n4\n10\n", ["0.0", "4.0", "16.0", "100.0"]),
        ("1.5\n3.2\n-1\n0\n", ['2.25', '10.240000000000002', '1.0', '0.0']),
        ("", []),
        ("5", ["25.0"]),
        ("a\nb\nc\n", ["could not convert string to float: 'a\\n'"]),
        ("0\n0\n0\n0\n0\n0\n", ['0.0', '0.0', '0.0', '0.0', '0.0', '0.0']), #нули
        ("-2\n0\n-88\n10\n-1.5\n5.1", ['4.0', '0.0', '7744.0', '100.0', '2.25', '26.009999999999998']), #отрицательные
        ("0\n2\n4\n10\n12\n14\n16\n1\n3\n5\n6\n7\n8\n10\n14.2\n12.02\n",
         ['0.0', '4.0', '16.0', '100.0', '144.0', '196.0', '256.0',
          '1.0', '9.0', '25.0', '36.0', '49.0', '64.0', '100.0', '201.64', '144.4804'] ), #много чисел
        ("5151513265\n48949416841351561\n865418948941\n12122854184616",
         ['2.653808891947096e+19', '2.3960454091083917e+33',
          '7.489499571861452e+23', '1.4696359358146167e+26']), #большие числа

    ])
    def test_sq_files(self, create_file, output_file, file_contents, expected_output):
        create_file.write_text(file_contents)
        sq_files(create_file, output_file)

        # Чтение содержимого выходного файла
        result = output_file.read_text().splitlines()
        assert result == expected_output