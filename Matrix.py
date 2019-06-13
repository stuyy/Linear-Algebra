class Matrix:
    def __init__(self, *args):

        if len(args) == 0:
            raise Exception("Cannot be empty Matrix!")
        if self.valid_matrix([*args]):
            self.matrix = [*args]
        else:
            raise Exception("Invalid Matrix. All rows must have the same amount of columns")
    
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
        return
    else:
        t = transpose(b)
        
        i = 0
        new =  []
        for outer in t:
            col = []
            for inner in a:
                j = 0
                sum = 0
                for num in inner:
                    sum += num*outer[j]
                    j+=1
                col.append(sum)
            new.append(col)

        print(transpose(new))
                
                
            
