from typing import Sequence

def binary_search(
        value: int, seq: Sequence[int],
        left_border: int = 0, right_border: int = None
) -> int:
    """
    Выполняет бинарный поиск заданного элемента внутри отсортированного массива

    :param value: Элемент, который надо найти
    :param seq: Массив, в котором будет производиться поиск
    :param left_border: Левая граница массива, нужна для рекурсивного алгоритма
    :param right_border: Правая граница массива, нужна для рекурсивного алгоритма

    :raise: ValueError если элемента нет в массиве
    :return: Индекс элемента в массиве
    """

    if right_border is None:
        right_border = len(seq) - 1

    # Базовый случай рекурсии
    if left_border > right_border:
        raise ValueError(f"Элемент {value} отсутствует в массиве")

    mid = left_border + (right_border - left_border) // 2

    if seq[mid] == value:
        # Если это самый первый элемент массива или элемент слева меньше искомого,
        # значит mid — это действительно первое вхождение.
        if mid == 0 or seq[mid - 1] < value:
            return mid
        # Иначе продолжаем искать левее, чтобы найти самое первое вхождение
        return binary_search(value, seq, left_border, mid - 1)

    if seq[mid] > value:
        return binary_search(value, seq, left_border, mid - 1)

    return binary_search(value, seq, mid + 1, right_border)

