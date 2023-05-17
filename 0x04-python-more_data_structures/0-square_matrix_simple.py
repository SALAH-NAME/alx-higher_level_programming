#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
