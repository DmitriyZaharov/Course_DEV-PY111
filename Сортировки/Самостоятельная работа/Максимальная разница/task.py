from typing import List
import math


def maximum_gap(nums: List[int]) -> int:
    """
    Находит максимальную разницу между последовательными элементами
    в отсортированном виде за линейное время O(N).
    """
    # Если элементов меньше двух, по условию возвращаем 0
    if len(nums) < 2:
        return 0

    min_val = min(nums)
    max_val = max(nums)
    n = len(nums)

    # Если все элементы в массиве одинаковые, максимальный зазор равен 0
    if min_val == max_val:
        return 0

    # Вычисляем размер одного ведра (bucket_size) по формуле ceiling[(max - min) / (n - 1)]
    # Используем целочисленное деление с округлением вверх
    bucket_size = math.ceil((max_val - min_val) / (n - 1))

    # Количество ведер (нам достаточно n ведер, чтобы покрыть весь диапазон)
    bucket_count = n

    # Инициализируем массивы для хранения минимумов и максимумов в каждом ведре
    # None означает, что ведро пока пустое
    bucket_mins = [None] * bucket_count
    bucket_maxs = [None] * bucket_count

    # Распределяем элементы по ведрам
    for num in nums:
        # Индекс ведра для текущего числа
        bucket_idx = (num - min_val) // bucket_size

        # Обновляем минимум в ведре
        if bucket_mins[bucket_idx] is None or num < bucket_mins[bucket_idx]:
            bucket_mins[bucket_idx] = num

        # Обновляем максимум в ведре
        if bucket_maxs[bucket_idx] is None or num > bucket_maxs[bucket_idx]:
            bucket_maxs[bucket_idx] = num

    # Вычисляем максимальный зазор между ведрами
    max_gap = 0
    # Предыдущим максимумом инициализируем максимум первого ведра (там точно лежит min_val)
    previous_max = bucket_maxs[0]

    for i in range(1, bucket_count):
        # Пропускаем пустые ведра
        if bucket_mins[i] is None:
            continue

        # Зазор — это разница между минимумом текущего ведра и максимумом предыдущего непустого ведра
        current_gap = bucket_mins[i] - previous_max
        max_gap = max(max_gap, current_gap)

        # Обновляем предыдущий максимум для следующей итерации
        previous_max = bucket_maxs[i]

    return max_gap

