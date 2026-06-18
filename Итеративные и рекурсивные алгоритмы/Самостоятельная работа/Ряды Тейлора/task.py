from typing import Union
from itertools import count
import math

DELTA = 0.000001


def sinx(x: Union[int, float]) -> float:
    """
    Вычисление sin(x) с помощью разложения в ряд Тейлора

    :param x: x значение в радианах
    :return: значение sin(x)
    """
    # Приводим x к диапазону [-pi, pi] для точности и быстрой сходимости
    x = math.fmod(x, 2 * math.pi)
    if x > math.pi:
        x -= 2 * math.pi
    elif x < -math.pi:
        x += 2 * math.pi

    # Инициализация для первого члена ряда (n = 0)
    # Первый член равен x, так как: ((-1)**0 * x**(2*0 + 1)) / (2*0 + 1)! = x / 1 = x
    current_term = x
    sin_sum = current_term

    # Начинаем со следующего шага (n = 1)
    for n in count(1):
        # Коэффициент перехода от предыдущего члена ряда к следующему:
        # -x^2 / ((2n) * (2n + 1))
        multiplier = -(x ** 2) / ((2 * n) * (2 * n + 1))
        current_term *= multiplier

        sin_sum += current_term

        # Если модуль текущего члена стал меньше DELTA, останавливаемся
        if abs(current_term) < DELTA:
            break

    return sin_sum

