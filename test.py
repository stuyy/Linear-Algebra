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

tm6 = transpose(m6)
print(tm6)

m7 = Matrix([2],[3],[4]).matrix
print(transpose(m7))

print(transpose(Matrix([4,4,4,4],[4,2,3,45]).matrix))

m8 = Matrix([2, 3, 4])
m9 = Matrix([2, 3])

try:
    dot_product(m8.matrix, m9.matrix)
except Exception as error:
    print(error)

m10 =  Matrix([2,3,4],[1,7,6]).matrix
m11 = Matrix([3,1,2],[2,2,7],[4,3,6]).matrix

dot_product(m10, m11)