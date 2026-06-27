from typing import List


def generate_pascal_triangle(num_rows: int) -> List[List[int]]:
    """
    Для генерации первых num_rows строк треугольника Паскаля необходимо последовательно формировать
    каждую строку, где каждый элемент (кроме первого и последнего) равен сумме двух элементов,
    стоящих над ним в предыдущей строке.
    """
    """Генерируем первые num_rows строк треугольника Паскаля."""
    # Если на вход подано 0 или отрицательное число, возвращаем пустой список
    if num_rows <= 0:
        return []

    # Инициализируем треугольник первой строкой
    triangle = [[1]]

    # Строим оставшиеся строки до num_rows
    for i in range(1, num_rows):
        prev_row = triangle[i - 1]
        # Каждая строка начинается с 1
        current_row = [1]

        # Заполняем внутренние элементы текущей строки
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # Каждая строка заканчивается на 1
        current_row.append(1)

        # Добавляем готовую строку в треугольник
        triangle.append(current_row)

    return triangle


if __name__ == "__main__":
    print(generate_pascal_triangle(5))
    print(
        f"Input: num_rows = 5\nOutput: {generate_pascal_triangle(5)}\n"
    )  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(f"Input: num_rows = 1\nOutput: {generate_pascal_triangle(1)}")  # [[1]]
