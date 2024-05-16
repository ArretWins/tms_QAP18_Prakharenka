# Работа с переменными:
var_int = 10
var_float = 8.14
var_str = "No"

big_int = var_int * 3.5
var_float = var_float - 1

print(var_int / var_float)  #tut ne uveren
print(big_int / var_float)  #tut ne uveren

var_str = "No" * 2 + "Yes" * 3
print(var_str, var_float, var_str, big_int, sep="\n")


# Строки:
def_str = "I live in Kosice"
fchar = def_str[0]
lchar = def_str[-1]
tchar = def_str[2]
techar = def_str[-3]

string_len = len(def_str)
print(string_len)

def_str2 = "Minsk-Kosice"
len_of_str = len(def_str2) // 2
sr1 = def_str2[:8]
sr2 = def_str2[len_of_str - 2: len_of_str + 2]
sr3 = def_str2[::3]
sr4 = def_str2[::-1]
print(sr1, sr2, sr3, sr4)

first_string = "my name is name"
print(first_string[:10] + first_string[10:].replace("name", "Artem"))

test_string = "Hello world!"
print(test_string.find("w"), test_string.count("l"), test_string.startswith("Hello"), test_string.endswith("qwe"),
      sep="\n")


# Списки:
sp1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
sp2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

sp1_2 = sp1[1]

sp2[-1] = '88'
print(sp2)

sp3 = sp1 + sp2
print(sp3)

slice_combined = sp3[1:5] + sp3[-3:-1]
print(slice_combined)
slice_combined.append('zZ')
slice_combined.append('cC')
print(slice_combined)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list(set(a).intersection(b))
print(common_elements)

c = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
new_c = list(set(c))
print(new_c)


# Логические операции:
fp = 3
sp = 5
exp1 = (fp < sp) and (sp < fp + sp)
exp2 = (fp > sp) and (sp < fp + sp)
exp3 = (fp == sp) and (sp < fp + sp)
exp4 = (fp != sp) and (sp < fp + sp)
print(exp1, exp2, exp3, exp4)
exp5 = (fp == sp) or (sp > fp + sp)
exp6 = (fp != sp) or (sp > fp + sp)
print(exp5, exp6)

str1 = "hello"
str2 = "world"
exp7 = (len(str1) > 3) and (len(str2) > 3)
exp8 = (str1.startswith("h")) or (str2.endswith("d"))
exp9 = (str1.isnumeric()) or (str2.isnumeric())
exp10 = (str1.islower()) and (str2.isupper())
print(exp7, exp8, exp9, exp10)


# Словари:
school = {
    '1а': 25,
    '1б': 30,
    '2а': 28,
    '2б': 29,
    '3а': 27,
    '5а': 5,
    '6б': 10,
    '4а': 8,
    '7a': 9,
    '7б': 7,
}

print(school['4а'])
school['1а'] = 22
school['1б'] = 12
school['2б'] = 11

school['9а'] = 5
school['10а'] = 4

school.pop('7б')

print(school)


# Преобразование типов
rs = "Robin Singh"
array1 = rs.split(" ")
ilove = "I love arrays they are my favorite"
array2 = ilove.split(" ")
array3 = ['Ivan', 'Ivanov']
city = "Minsk"
country = "Belarus"
print(f"Привет, {array3[0]} {array3[1]}! Добро пожаловать в {city} {country}")
ilove2 = " ".join(array2)
print(ilove2)
new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list.insert(2, 9)
new_list.pop(6)
print(new_list)

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {}
for key in sorted((a.keys()) | set(b.keys())):
    value_a = a.get(key)
    value_b = b.get(key)
    ab[key] = [value_a, value_b]
print(ab)

array4 = [1, 5, 2, 9, 2, 9, 1]
counts = {}
for num in array4:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num, count in counts.items():
    if count < 2:
        print(num)


# Условия
a = 5
if a > 0:
    a += 1
print(a)

b, c = 1, -2
counter = 0
if a > 0:
    counter += 1
if b > 0:
    counter += 1
if c > 0:
    counter += 1
print(counter)

year = 2023
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_year = 366
else:
    days_in_year = 365
print(days_in_year)

day = 3
days_of_week = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье"
]
print(days_of_week[day - 1])

u_number = 1
weight = 1200.0
unit_to_kg = {
    1: 1,  # килограмм
    2: 0.000001,  # миллиграмм
    3: 0.001,  # грамм
    4: 1000,  # тонна
    5: 100  # центнер
}
weight_in_kg = weight * unit_to_kg[u_number]
print(weight_in_kg)


#Цикл for
a = 4
b = 7
c = 0
counter = 0
for num in range(a, b + 1):
    counter += num
print(counter)

nat_count = 0
for num in range(a, b + 1):
    if num > 0:
        nat_count += num
print(nat_count)

product_positives, sum_negatives, count_negatives = 1, 0, 0

for i in range(10):
    num = int(input(f"Введите {i + 1}-е число: "))
    if num > 0:
        product_positives *= num
    elif num < 0:
        sum_negatives += num
        count_negatives += 1

if count_negatives == 10:
    product_positives = 0

print("Пр-е положительных:", product_positives)
print("Сумма отрицательных:", sum_negatives)
print("Кол-во отрицательных:", count_negatives)

swimmers = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}

best_result = max(swimmers.values())
print(best_result)

array4 = [1, 5, 2, 9, 2, 9, 1]
counts = {}
for num in array4:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num, count in counts.items():
    if count < 2:
        print(num)


# Цикл while
n = 4
i = 1
res = 1
while i != n + 1:
    res *= i
    i += 1
print(res)

S1, S2 = 2, 4
years = 0
while S1 >= 0.1 * S2:
    S1 *= 2
    S2 *= 3
    years += 1
print(years)

n = 25
count_digits, sum_digits = 0, 0
while n > 0:
    digit = n % 10
    count_digits += 1
    sum_digits += digit
    n //= 10
print(count_digits, sum_digits)

m = 60
n = 10
x = 0
while n * 2 != m:
    x += 1
    m += 1
    n += 1

print(x, n, m)
