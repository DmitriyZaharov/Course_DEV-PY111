from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Находит индексы двух чисел, которые в сумме дают target.

    :param nums: Список целых чисел
    :param target: Целевая сумма
    :return: Список из двух индексов
    """
    # Словарь для хранения пар {число: его_индекс}
    seen = {}

    for index, num in enumerate(nums):
        # Ищем число, которого не хватает до target
        complement = target - num

        # Если такое число уже встречалось, возвращаем его индекс и текущий индекс
        if complement in seen:
            return [seen[complement], index]

        # Если не встречалось, сохраняем текущее число и его индекс
        seen[num] = index

    # По условию задачи решение всегда существует, поэтому сюда код не дойдет
    raise ValueError("Решение не найдено")
