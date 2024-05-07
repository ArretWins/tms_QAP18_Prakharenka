# Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

def sq_files(file):
    try:
        with open(file, 'r') as f:
            numbers = [float(num) for num in f.readlines()]

            squared_numbers = [num ** 2 for num in numbers]

            with open('file.txt', 'w') as nf:
                for squared_num in squared_numbers:
                    nf.write(str(squared_num) + '\n')
            print("Done.")

    except Exception as e:
        print(e)


sq_files('file.txt')
