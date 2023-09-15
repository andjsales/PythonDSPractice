def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    sum1 = 0
    sum2 = 0

    rows = len(matrix)

    for i in range(rows):
        sum1 += matrix[i][i]
        sum2 += matrix[i][rows - i - 1]
    return sum1 + sum2


m1 = [
     [1,   2],
     [30, 40],
]

sum_up_diagonals(m1)
# 73

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
sum_up_diagonals(m2)
# 30
