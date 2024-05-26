#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []

    result = []

    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        result.append(new_row)

    return result
