from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Проверяет, содержит ли массив дубликаты.

    :param nums: Список целых чисел
    :return: True, если элементы повторяются, иначе False
    """
    # Если длина множества уникальных элементов меньше длины списка,
    # значит в исходном массиве были дубликаты.
    return len(nums) != len(set(nums))

"""
    Вариант ниже работает быстрее в таких случаях, так как останавливается сразу при 
    первом обнаружении дубликата:
"""

def contains_duplicate_fast(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
