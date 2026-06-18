from typing import List

def missing_number(nums: List[int]) -> int:
    """
    Находит отсутствующее число с помощью формулы суммы арифметической прогрессии.
    """
    n = len(nums)
    # Формула суммы Гаусса для чисел от 0 до n
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

"""
Свойство XOR: X ^ X = 0 и X ^ 0 = X. Если мы применим XOR ко всем индексам от 0 до n и ко 
всем числам в массиве, то все присутствующие числа «уничтожат» друг друга, а останется только 
отсутствующее.
"""

def missing_number_xor(nums: List[int]) -> int:
    """
    Находит отсутствующее число с помощью побитовой операции XOR.
    """
    missing = len(nums)

    # Применяем XOR к индексам и значениям одновременно
    for i, num in enumerate(nums):
        missing ^= i ^ num

    return missing

