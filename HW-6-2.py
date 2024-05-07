# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.


def mixed_files(file):
    try:
        with open(file, 'r') as f:
            nums = [int(num) for num in f.readlines()]
            even = [num for num in nums if num % 2 == 0]
            not_even = [num for num in nums if num % 2 != 0]
            with open('even.txt', 'w') as file:
                if len(even) > 0:
                    for num in even:
                        file.write(str(num) + '\n')
                        file.flush()
                        # file.close()
            with open('not_even.txt', 'w') as file:
                if len(not_even) > 0:
                    for num in not_even:
                        file.write(str(num) + '\n')
                        file.flush()
                        # file.close()
            f.flush()
            f.close()
            print("Done!")
    except Exception as e:
        print(e)


mixed_files('first.txt')
