
from typing import List

"""
Поскольку в условии задачи сказано, что каждый элемент в результате должен быть уникальным,
перевод массивов во множества автоматически убирает дубликаты и позволяет найти пересечение 
за линейное время.
"""

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Находит уникальные элементы, которые присутствуют в обоих массивах.

    :param nums1: Первый массив целых чисел
    :param nums2: Второй массив целых чисел
    :return: Список уникальных элементов пересечения
    """
    # Превращаем массивы во множества и находим их пересечение оператором &
    return list(set(nums1) & set(nums2))


def intersection_manual(nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    result = set()

    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)
