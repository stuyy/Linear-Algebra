import numpy as np
from Matrix import *

m = Matrix([3, 4, 5], [2, 3, 4], [5, 6, 7], [8, 9, 0])

print(m.matrix)

matrix_a = [
    [1, 0, 1],
    [2, 3, 4],
    [2, 4, 6]
]

matrix_b = [
    [2, 4, 6],
    [3, 4, 6],
    [3, 1, 2]
]

def valid_matrix(matrix):

    if len(matrix) == 0:
        return True
    elif len(matrix) == 1:
        return True
    else:
        row = matrix[0]
        return validate(matrix, len(row))

def validate(check, length_of_row):

    if len(check) == 1:
        return len(check[0]) == length_of_row

    curr_row = check.pop(0)
    if len(curr_row) != length_of_row:
        return False
    else:
        return validate(check, length_of_row)


print(valid_matrix(matrix_a))
print(valid_matrix(matrix_b))