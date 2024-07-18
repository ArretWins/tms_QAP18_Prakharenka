# Написать для 3 и 4 задания в HW 5 тесты (полные покрытие) и 1 и 3 задание в HW 6
# 1 Параметризация
# 2 Фикстуры (для открытия и закрытия файлов) для HW 6
# 3 Использовать mark для разного запуска тестов
# 4* Исправить код оригинального задания так чтобы проходил без ошибок

# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

from pytest import mark, fixture


def read_files(file):
    try:
        with open(file, 'r') as f:
            nums = [int(num) for num in f.readlines()]
            if len(nums) < 4:
                raise ValueError("Файл содержит меньше 4 чисел")
            return nums[0], nums[1], nums[-2], nums[-1]
    except Exception as e:
        return str(e)


class TestHw6:
    @fixture
    def create_file(self, tmp_path):
        file_path = tmp_path / "test_file.txt"
        yield file_path
        file_path.unlink()

    @mark.hw6_1
    @mark.parametrize("file_contents, expected_output", [
        ("0\n2\n4\n10\n", (0, 2, 4, 10)),
        ("1\n3\n44\n5\n15\n44\n5\n174\n5\n15\n41\n1\n15\n8\n7\n9\n", (1, 3, 7, 9)),#много чисел
        ("1541548123168513\n132132123131\n10\n6464686468468464\n1000\n5464564514",
         (1541548123168513, 132132123131, 1000, 5464564514)),#больШие числа
        ("-1\n-2\n-3\n-4\n", (-1, -2, -3, -4)),     #отрицательные числа
        ("0\n0\n0\n0\n0\n0", (0, 0, 0, 0)),     #добавил нули
        ("!\n!\n!\n!\n!\n!", "invalid literal for int() with base 10: '!\\n'"),     #Проверка на специальные символы
        ("1.2\n1.001\n55\n78.78\n23\n54", "invalid literal for int() with base 10: '1.2\\n'"),     #Проверка на дроби
        ("1\n2\n", "Файл содержит меньше 4 чисел"),
        ("", "Файл содержит меньше 4 чисел"),
        ("a\n2\ncds\n8\n56", "invalid literal for int() with base 10: 'a\\n'")
    ])
    def test_read_files(self, create_file, file_contents, expected_output):
        create_file.write_text(file_contents)
        assert read_files(create_file) == expected_output


