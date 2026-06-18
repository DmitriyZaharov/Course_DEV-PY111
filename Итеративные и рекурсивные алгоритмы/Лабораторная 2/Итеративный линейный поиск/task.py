"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # Если массив пустой, возвращаем -1 или вызываем исключение (в зависимости от требований)
    if not arr:
        raise ValueError("min_search() arg is an empty sequence")

    # Инициализируем индекс минимального элемента нулем
    min_index = 0

    # Перебираем массив, начиная со второго элемента (индекс 1)
    for i in range(1, len(arr)):
        # Строгое сравнение "<" гарантирует поиск ИМЕННО ПЕРВОГО вхождения.
        # Если встретится дубликат минимума, условие не выполнится, и индекс не перезапишется.
        if arr[i] < arr[min_index]:
            min_index = i

    return min_index
