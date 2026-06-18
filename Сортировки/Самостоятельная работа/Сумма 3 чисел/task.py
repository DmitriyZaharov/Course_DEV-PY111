from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Находит все уникальные триплеты в массиве, сумма которых равна 0.

    :param nums: Список целых чисел
    :return: Список уникальных триплетов
    """
    # 1. Сортируем массив. Это нужно для работы указателей и пропуска дубликатов.
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        # Если текущее число больше 0, то сумма с последующими (которые еще больше)
        # никак не сможет стать равной 0. Выходим из цикла.
        if nums[i] > 0:
            break

        # Пропускаем дубликаты для первого элемента триплета
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 2. Инициализируем два указателя для поиска оставшихся двух чисел
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                res.append([nums[i], nums[left], nums[right]])

                # Пропускаем дубликаты для второго элемента триплета
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Пропускаем дубликаты для третьего элемента триплета
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Сдвигаем оба указателя после успешного нахождения
                left += 1
                right -= 1

            elif current_sum < 0:
                # Сумма слишком маленькая — сдвигаем левый указатель вправо (к большим числам)
                left += 1
            else:
                # Сумма слишком большая — сдвигаем правый указатель влево (к меньшим числам)
                right -= 1

    return res
