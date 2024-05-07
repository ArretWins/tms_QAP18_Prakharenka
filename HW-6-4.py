# 4 Даны два файла произвольного типа. Поменять местами их содержимое. Файлы должны быть бинарного типа

def bin_files(file1, file2):
    try:
        with open(file1, 'rb') as file1:
            data1 = file1.read()
        with open(file2, 'rb') as file2:
            data2 = file2.read()
        with open('file1.bin', 'wb') as file1:
            file1.write(data2)
        with open('file2.bin', 'wb') as file2:
            file2.write(data1)

        print('Binary files have been written successfully.')

    except Exception as e:
        print(e)


bin_files('file1.bin', 'file2.bin')
