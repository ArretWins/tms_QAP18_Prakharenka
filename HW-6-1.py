# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

def read_files(file):
    try:
        with open(file, 'r') as f:
            nums = [int(num) for num in f.readlines()]
            if len(nums) < 4:
                raise ValueError("Файл содержит меньше 4 чисел")

            print("Первый элемент:", nums[0])
            print("Второй элемент:", nums[1])
            print("Предпоследний элемент:", nums[-2])
            print("Последний элемент:", nums[-1])
    except Exception as e:
        print(e)


read_files('first.txt')
