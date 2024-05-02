#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(row):
        return list(map(lambda x: x * x, row))
    return list(map(square, matrix))
