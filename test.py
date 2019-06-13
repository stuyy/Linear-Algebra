import numpy as np
from Matrix import *

m = Matrix([3, 4, 5], [2, 3, 4], [5, 6, 7])
m2 = Matrix([2, 3], [2, 4], [22, 34])

print(np.dot(m.matrix, m2.matrix))

m3 = Matrix([3,4,5], [3, 0, 7],[7,2,2]).matrix
m4 = Matrix([3,1], [2,0], [0,2]).matrix

print(np.dot(m3, m4))

m5 = Matrix([2,4,6],[8,2,7]).matrix
m6 = Matrix([2, 3],[1, 2],[2, 4]).matrix
print(np.dot(m5, m6))


def transpose(matrix):
    def initialize(rows, columns):
        matrix = []
        for x in range(rows):
            matrix.append([])
            for y in range(columns):
                matrix[x].insert(y, 0)
        
        return matrix

    def _transpose(initial_matrix, result):
        rows=len(result)
        cols=len(result[0])
        for i in range(rows):
            for j in range(cols):
                result[i][j] = initial_matrix[j][i]

        return result
    init_matrix = initialize(len(matrix[0]),len(matrix))
    return _transpose(matrix, init_matrix)

# Length of Matrix is the number of rows. So that means there will be len(matrix) of columns in the transpose.

arr = []

arr.insert(5, 2)
transpose_of_m6 = transpose(m6)
print(m6)
print(transpose_of_m6)