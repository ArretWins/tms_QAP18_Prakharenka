import time

# 1 Написать обычную функцию для факториала, генератор и рекурсию. Сравнить их время работы
n = 10
iterations = 5000
start_time = time.perf_counter()


# Casual func
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Generator
def factorial_generator(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
        yield result


def factorial_gen_result(n):
    result = 1
    for value in factorial_generator(n):
        result = value
    return result


# Rekursia
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Dlya obicnoj rekursii
for _ in range(iterations):
    factorial_iterative(n)
iterative_time = time.perf_counter() - start_time

# Dlya funkcii s generatorom
for _ in range(iterations):
    factorial_gen_result(n)
generator_time = time.perf_counter() - start_time

# Dlya rekusii
for _ in range(iterations):
    factorial_recursive(n)
recursive_time = time.perf_counter() - start_time


print(f"Время выполнения обычной функции: {iterative_time:.4f} секунд")
print(f"Время выполнения функции с генератором: {generator_time:.4f} секунд")
print(f"Время выполнения рекурсивной функции: {recursive_time:.4f} секунд")


# 2 Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
def typed(type='str'):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if type == 'str':
                target_type = str
            elif type == 'int':
                target_type = int
            elif type == 'float':
                target_type = float
            else:
                raise ValueError(f"Unsupported type: {type}")

            new_args = [target_type(arg) for arg in args]
            return func(*new_args, **kwargs)
        return wrapper
    return decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


@typed(type='int')
def add_three_symbols(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    else:
        # я не понимаю почему он не выводит в этой функции 0.70000 а 0.0 поэтому сделаю отдельную функцию для дробей
        # наверное так как выше мы обозначем что тип будет ИНТ мы получаем их именно целыми числами (то есть нулями)
        return f"{float(a) + float(b) + float(c):.7f}"


@typed(type='float')
def add_three_floats(a, b, c):
    return a + b + c


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_floats(0.1, 0.2, 0.4))
print(add_three_symbols(0.1, 0.2, 0.4))
