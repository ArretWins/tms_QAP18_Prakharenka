# 1 Напишите функцию is_year_leap, которая принимает число (год) и возвращает true, если год високосный false если нет.

def is_year_leap(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


print(is_year_leap(2000))
