# Linear Algebra

## Linear Algebra Library written in Python


# Documentation

## *class* Matrix

A representation of a Matrix as a 2-dimensional list.

`size_of_matrix(): string` - returns the string representation in *m* x *n* form
`validate(matrix, num_cols)` - Validates the Matrix ensuring it is not a ragged Matrix.

----

The Matrix.py module has other functions that need not be called on an instance of a Matrix. This is useful if you prefer using 2D lists

`transpose(matrix: Matrix)`: tranposed_matrix - returns a transposed matrix of the original. THis does not modify the original matrix.

`dot_product(m1: Matrix, m2: Matrix)`: matrix - returns the dot product of two matrices
