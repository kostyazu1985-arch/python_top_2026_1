"""
1. Посчитать количествол символов в тексте
2. Посчитать количество слов в тексте
3. Посчитать количество строк в тексте
4. Посчитать количество гласных, согласных, спец символов
5. Статистический анализ букв ( частота встречаемости символов)
"""


def get_text_from_file(path_text_file: str)-> str:
    """
    получает текст из файла (get text content from file)
    :param path_text_file: file path of text file
    :return: the text content of the file
    """
    with open(path_text_file, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def get_count_characters(text: str)-> int:
    """
    Get count of characters in text
    :param text: text content
    :return: count of characters in text
    """
    count_characters = len(text)
    return count_characters

def get_count_words(text: str)-> int:
    """
    Get count of words in text
    :param text: text content
    :return: count of words in text
    """
    count_words = len(text.split())
    return count_words

def get_count_lines(text: str)-> dict:
    lines = text.split("\n")
    count_lines = len(lines)
    count_empty_lines = 0
    for i in lines:
        if i == "":
            count_empty_lines += 1
    result = {
        "empty_lines": count_empty_lines,
        "non_empty_lines": count_lines - count_empty_lines,
        "lines": count_lines,
    }
    return result


def get_stat_symbols(text: str)-> dict:
    vowels = "аоуэиыеёюя"
    consonats = "бвгджзйклмнпрстфхцчшщ"
    spec_symbols = ".,!?-:\'\"%(){}<>;+=*"
    vowels_count = 0
    consonats_count = 0
    spec_count = 0
    for i in text:
        # если гласная
        if i.lower() in vowels:
            vowels_count += 1
        # если согласная
        elif i.lower() in consonats:
            consonats_count += 1
        # если спец символ
        elif i.lower() in spec_symbols:
            spec_count += 1
    result = {
        "vowels_count": vowels_count,
        "consonats_count": consonats_count,
        "spec_symbols_count": spec_count,
    }
    return result

# abaacb
def get_character_frequency(text:str)-> dict:
    """
    Get frequency of characters in text
    :param text: text content
    :return: frequency of characters in text
    """
    character_frequency = {}
    for i in text.lower():
        if i in character_frequency:
            character_frequency[i] += 1
        else:
            character_frequency[i] = 1
    return character_frequency


def get_character_frequency_2(text:str)-> dict:
    """
    Get frequency of characters in text
    :param text: text content
    :return: frequency of characters in text
    """
    character_frequency = {}
    for i in text.lower():
        if i in character_frequency:
            continue
        count = text.lower().count(i)
        character_frequency[i] = count
    return character_frequency


if __name__ == "__main__":
    print("Это код файла text_utils.py")
    print(__name__)

text = get_text_from_file(path_text_file="Poema.txt")
count_characters = get_count_characters(text)
count_words = get_count_words(text)
count_lines = get_count_lines(text)
stat_symbols = get_stat_symbols(text)
frequency = get_character_frequency(text)


print("Количество символов в тексте - ", count_characters)
print("Количество слов в тексте - ", count_words)
print("Количество строк в тексте\n", *count_lines.items())
print("Анализ символов в тексте\n", *stat_symbols.items())

for i in frequency:
    print(f"{i}: {frequency[i]}")