# Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.
import os

from pytest import mark, fixture


@fixture
def read_file():
    def _read_file(file):
        with open(file, 'r') as f:
            numbers = []
            for line in f:
                try:
                    numbers.append(float(line.strip()))
                except ValueError as e:
                    raise ValueError(f"could not convert string to float: '{line.strip()}'")
            return numbers
    return _read_file


@fixture
def write_file():
    def _write_file(output_file, squared_numbers):
        with open(output_file, 'w') as nf:
            for squared_num in squared_numbers:
                nf.write(str(squared_num) + '\n')
    return _write_file


def sq_files(numbers):
    return [num ** 2 for num in numbers]


class TestHw6:
    @mark.hw6_3
    @mark.parametrize("file_contents, expected_output", [
        ("0\n2\n4\n10\n", ["0.0", "4.0", "16.0", "100.0"]),
        ("1.5\n3.2\n-1\n0\n", ['2.25', '10.240000000000002', '1.0', '0.0']),
        ("", []),
        ("5", ["25.0"]),
        # ("a\nb\nc\n", ["could not convert string to float: 'a'"]),
        ("0\n0\n0\n0\n0\n0\n", ['0.0', '0.0', '0.0', '0.0', '0.0', '0.0']), #нули
        ("-2\n0\n-88\n10\n-1.5\n5.1", ['4.0', '0.0', '7744.0', '100.0', '2.25', '26.009999999999998']), #отрицательные
        ("0\n2\n4\n10\n12\n14\n16\n1\n3\n5\n6\n7\n8\n10\n14.2\n12.02\n",
         ['0.0', '4.0', '16.0', '100.0', '144.0', '196.0', '256.0',
          '1.0', '9.0', '25.0', '36.0', '49.0', '64.0', '100.0', '201.64', '144.4804'] ), #много чисел
        ("5151513265\n48949416841351561\n865418948941\n12122854184616",
         ['2.653808891947096e+19', '2.3960454091083917e+33',
          '7.489499571861452e+23', '1.4696359358146167e+26']), #большие числа

    ])
    def test_sq_files(self, read_file, write_file, file_contents, expected_output, tmp_path):
        input_file = tmp_path / "numbers.txt"
        output_file = tmp_path / "output_numbers.txt"

        input_file.write_text(file_contents)

        try:
            numbers = read_file(input_file)
            squared_numbers = sq_files(numbers)
            write_file(output_file, squared_numbers)
            result = output_file.read_text().splitlines()
        except ValueError as e:
            result = [str(e)]


        assert result == expected_output

        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file_path = os.path.join(output_dir, "output_numbers.txt")
        with open(output_file_path, 'w') as f:
            for squared_num in squared_numbers:
                f.write(str(squared_num) + '\n')