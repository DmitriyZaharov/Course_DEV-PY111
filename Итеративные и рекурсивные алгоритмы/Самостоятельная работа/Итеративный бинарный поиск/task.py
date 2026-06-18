from typing import Sequence


def binary_search(value: int, seq: Sequence) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    Первое вхождение: Строка right = mid - 1 сдвигает границу влево при совпадении.
    Это гарантирует, что мы найдем самое раннее появление дубликата.
    Экономия памяти: O(1) — в отличие от рекурсии, здесь не создаются новые фреймы в стеке вызовов
    Скорость: O(log n) — область поиска уменьшается в два раза на каждой итерации.

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """
    left, right = 0, len(seq) - 1
    result_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if seq[mid] == value:
            result_index = mid  # Запоминаем текущую позицию
            right = mid - 1     # Продолжаем искать левее для поиска первого вхождения
        elif seq[mid] > value:
            right = mid - 1
        else:
            left = mid + 1

    if result_index == -1:
        raise ValueError(f"Элемент {value} отсутствует в массиве")

    return result_index

