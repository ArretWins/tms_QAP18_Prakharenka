# 1 Создать lambda функцию, которая принимает на вход имя и выводит его в формате “Hello, {name}”
greeting = lambda x: f"Hello, {x}"
print(greeting("Artem"))

# 2 Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список
all_greeting = lambda names: list(map(lambda x: greeting(x), names))
all_names = ["Artem", "Elena", "Mark", "Vitek"]
greetings = all_greeting(all_names)
print(greetings)


# 1 Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и озвращает новый список только с положительными числами
def create_generator(numbers):
    new_numbers = [number for number in numbers if number >= 0]
    for number1 in new_numbers:
        yield number1


my_numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
my_generator = create_generator(my_numbers)

for number in my_generator:
    print(number)


# 2 Необходимо составить список чисел которые указывают на длину слов в строке:
# sentence = " the quick brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений
def get_length_of_words_in_sentence(sentence):
    try:
        words = sentence.split()
        lenths = [len(words) for words in words if words.upper() != 'THE']
        return lenths
    except Exception as e:
        return print(e)


my_sentence = "the quick brown fox jumps over the lazy dog"
my_words = get_length_of_words_in_sentence(my_sentence)
print(my_words)


# Шифр Цезаря * — один из древнейших шифров. При шифровании каждый символ заменяется другим, отстоящим
# от него в алфавите на фиксированное число позиций.
# ● hello world! -> khoor zruog!
# ● this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
def encode(text: str, shift: int) -> str:
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encode_text = ''
    for letter in text:
        if letter.islower():
            encode_char = alphabet_lower[(alphabet_lower.index(letter) + shift) % 26]
        elif letter.isupper():
            encode_char = alphabet_upper[(alphabet_upper.index(letter) + shift) % 26]
        else:
            encode_char = letter
        encode_text += encode_char

    return encode_text


def decode(text: str, shift: int) -> str:
    return encode(text, -shift)


print(encode("papa", 2))
print(decode("rcrc", 2))