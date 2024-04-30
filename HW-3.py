#1
a = 1.69
b = 2.99

#2
string1 = 'www.my_site.com#about'
string2 = string1.replace('#', '/')
print(string2)

#3
string3 = "stroka"
string31 = string3 + "ing"
print(string31)

#4
string4 = 'Ivanou Ivan'
words = string4.split(' ')
string41 = " ".join(reversed(words))
print(string41)

#5
string5 = '   Tut est probiely   '
string51 = string5.strip()
print(string51)

#6
school = {'1a': 15, '1b': 8, '1c': 12, '2a': 8, '2b': 18, '3a': 8, '3b': 2, '4a': 5, '4b': 6, '5a': 11}
print(school)

#7
spisok = ['anis2', 'matematika', 'awt', 'jda']
print(spisok[2])

#8
string8 = "employ"
string81 = "employment"
print(string8 in string81)

#9
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:16:3]) #nesgt

#10
x = [1, 5, 2, 9, 2, 9, 1]
another_list = []

for i in x:
    if x.count(i) == 1:
        another_list.append(i)

print(another_list)
