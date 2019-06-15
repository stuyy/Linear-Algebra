class Matrix:
    def __init__(self, *args):

        if len(args) == 0:
            raise Exception("Cannot be empty Matrix!")
        if self.valid_matrix([*args]):
            self.matrix = [*args]
            self.rows = len(args)
            self.columns = len(args[0])
        else:
            raise Exception("Invalid Matrix. All rows must have the same amount of columns")
    def size_of_matrix(self):
        return str(self.rows) + 'x' + str(self.columns)
    def valid_matrix(self, matrix):
        if len(matrix) == 0:
            return True
        elif len(matrix) == 1:
            return True
        else:
            row = matrix[0]
            return self.validate(matrix, len(row))

    def validate(self, check, length_of_row):

        if len(check) == 1:
            return len(check[0]) == length_of_row

        curr_row = check.pop(0)
        if len(curr_row) != length_of_row:
            return False
        else:
            return self.validate(check, length_of_row)

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

"""def dot_product(a, b):
    if len(a[0]) != len(b):
        raise Exception("# of rows for matrix a is not equal to # of cols in matrix b!")
    else:
        t = transpose(a)
        for i in range(len(b)): # Iterate  number of rows times
            some =  []
            for j in range(len(t)): # j is the current row  of the transposed matrix
                temp = []
                for k in range(len(t[j])):
                    num = b[i][j]
                    multiplier = t[j][k]
                    print("Multiplying " + str(num) + " by " + str(multiplier))
                    temp.append(num*multiplier)
                some.append(temp)
                print(some)"""

def dot_product(a, b):
    if len(a[0]) != len(b):
        raise Exception("# of  rows for matrix a is not  equal to # of cols in matrix b!")
    else:
        t = transpose(b) # Transpose Matrix B
        new = [] # Initialize an empty array which will hold all columns
        i = 0
        for outer in t: # For every row in the Transpose of Matrix B
            col = [] # Initialize column matrix
            k = 0
            for inner in a: # For each row in Matrix A.
                j = 0 # Initialize j, our counter
                sum = 0 # Sum 
                for num in inner: # For each number in the current row of Matrix A.
                    sum += num*outer[j] # Take the current number in the current row of Matrix A, and multiply it with the outer row at subscript j.
                    # Essentially we are summing up and placing them in the right column.
                    j+=1
                col.append(sum) # Once we sum everything, we append to the column. Repeat loop for next row in Matrix A.
            new.append(col)

        return transpose(new)
                
def scale(matrix, scalar):
    newMatrix = []
    for rows in matrix:
        cols = []
        for entry in rows:
            cols.append(entry*scalar)
        newMatrix.append(cols)
    return newMatrix

def sum(matrix_a, matrix_b):
    if isinstance(matrix_a, Matrix) and isinstance(matrix_b, Matrix):
        newMatrix = []
        if matrix_a.size_of_matrix() == matrix_b.size_of_matrix():
            for i in range(len(matrix_a.matrix)):
                col = []
                for j in range(len(matrix_a.matrix[i])):
                    sum = matrix_a.matrix[i][j] + matrix_b.matrix[i][j]
                    col.append(sum)
                newMatrix.append(col)
            return newMatrix
        else:
            raise Exception("The size of both matrices must be the same!")
    else:
        raise Exception("Must be instances of a Matrix object")

def subtract(matrix_a, matrix_b):
    if isinstance(matrix_a, Matrix) and isinstance(matrix_b, Matrix):
        newMatrix = []
        if matrix_a.size_of_matrix() == matrix_b.size_of_matrix():
            for i in range(len(matrix_a.matrix)):
                col = []
                for j in range(len(matrix_a.matrix[i])):
                    diff = matrix_a.matrix[i][j] - matrix_b.matrix[i][j]
                    col.append(diff)
                newMatrix.append(col)
            return newMatrix
        else:
            raise Exception("The size of both matrices must be the same!")
    else:
        raise Exception("Must be instances of a Matrix object")

def inverse(matrix):
    if isinstance(matrix, Matrix):
        if is_square(matrix):
            if len(matrix.matrix) == 2:
                m = matrix.matrix
                a = m[0][0]
                b = m[0][1]
                c = m[1][0]
                d = m[1][1]
                det = (a*d)-(b*c)
                if det == 0:
                    return None
                else:
                    m[0][0] = d
                    m[1][1] = a
                    m[0][1] = 0-b
                    m[1][0] = 0-c
                    scalar = (1/((a*d)-(b*c)))
                    return scale(m, scalar)
    else:
        return None

def det(matrix):
    if isinstance(matrix, Matrix):
        if is_square(matrix):
            if len(matrix.matrix) == 2:
                m = matrix.matrix
                a = m[0][0]
                b = m[0][1]
                c = m[1][0]
                d = m[1][1]
                return (1/((a*d)-(b*c)))
            else:
                pass
    else:
        return None
def is_square(matrix):
    if isinstance(matrix, Matrix):
        return len(matrix.matrix) == len(matrix.matrix[0])

def get_sub_matrix(matrix, row, column):
    print("Give me the sub matrix at row " + str(row) + " column " + str(column))
    row -= 1
    column -=1
    newMatrix = []
    i = 0
    for rows in matrix:
        if i == row:
            pass
        else:
            j = 0
            newRow = []
            for num in rows:
                if j == column:
                    pass
                else:
                    newRow.append(num)
                j+=1
            newMatrix.append(newRow)
        i += 1
    
    return newMatrix