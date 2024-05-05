# 2 Напишите функцию generate_natural_cubes(n), которая принимает число n и возвращает список, состоящий
# из кубов первых n натуральных чисел. То есть [1**3, 2**3, 3**3, ..., n**3].
# Обязательно использование генераторов списков.

def generate_natural_cubes(n):
    return [i**3 for i in range(1, n+1)]


print(generate_natural_cubes(5))
