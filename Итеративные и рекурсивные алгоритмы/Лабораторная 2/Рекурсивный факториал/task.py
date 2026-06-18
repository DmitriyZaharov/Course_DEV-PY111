def factorial_recursive(n: int) -> int:
    """
    Вычислить факториал числа n рекурсивным алгоритмом.
    """
    # 1. Проверяем, что передано именно целое число (требуется для теста test_fact_rec_exc_float)
    if not isinstance(n, int):
        raise TypeError("Факториал определен только для целых чисел")

    # 2. Проверяем, что число неотрицательное
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    # 3. Базовый случай рекурсии
    if n == 0 or n == 1:
        return 1

    # 4. Рекурсивный шаг
    return n * factorial_recursive(n - 1)
