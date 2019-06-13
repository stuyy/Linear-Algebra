class Matrix:
    def __init__(self, *args):
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
