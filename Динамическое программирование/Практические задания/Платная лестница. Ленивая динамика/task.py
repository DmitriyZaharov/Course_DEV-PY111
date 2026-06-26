from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень

    Декоратор @lru_cache автоматически сохраняет каждый посчитанный get_min_cost(i) в таблицу памяти.
    Если этот индекс потребуется снова (например, при расчете других путей),
    Python мгновенно вернет готовое значение вместо повторного прохода по рекурсии.
    """
    ...  # TODO реализовать ленивую динамику
    # Если лестница пустая
    if not stairway:
        return 0

    @lru_cache(maxsize=None)
    def get_min_cost(i: int) -> Union[float, int]:
        # Базовые случаи: если стоим на 0-й или 1-й ступени,
        # платим только за саму эту ступень (это возможные точки старта)
        if i == 0:
            return stairway[0]
        if i == 1:
            return stairway[1]

        # Рекурсивный шаг: минимальная стоимость дойти до i-й ступени —
        # это цена самой i-й ступени плюс минимум из стоимостей её предшественников
        return stairway[i] + min(get_min_cost(i - 1), get_min_cost(i - 2))

    # Запускаем расчет с самого конца — с индекса последней ступени
    last_index = len(stairway) - 1
    return get_min_cost(last_index)

if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
