from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """
    Проверяет, является ли строка t анаграммой строки s.

    :param s: Исходная строка
    :param t: Строка для проверки
    :return: True, если t — анаграмма s, иначе False
    """
    # Если длины строк не равны, они точно не могут быть анаграммами
    if len(s) != len(t):
        return False

    # Сравниваем частотные словари букв для обеих строк
    return Counter(s) == Counter(t)


def is_anagram_manual(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    # Считаем символы первой строки
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Вычитаем символы второй строки
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False

    return True

"""
Если буквы в словах отсортировать по алфавиту, то у анаграмм получатся одинаковые строки.
"""
def is_anagram_sorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
