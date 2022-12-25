from random 
from copy 

class Matrix(object):

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = []

        for i in range(rows):
            self.matrix.append([]) # Initialize empty rows

        for row in self.matrix:
            for i in range(columns):
                row.append(randint(10)) # Fill the rows with random numbers

    def __add__(self, otherMatrix):
        return self.__add_or_sub(otherMatrix, "add")

    def __sub__(self, otherMatrix):
        return self.__add_or_sub(otherMatrix, "sub")

    def __add_or_sub(self, secondTerm, operation):
        newMatrix = Matrix(self.rows, self.columns)

        if isinstance(secondTerm, (int, float, complex)):
            for row in range(self.rows):
                for column in range(self.columns):
                    if operation == "add":
                        newMatrix[row][column] = self[row][column] + secondTerm
                    if operation == "sub":
                        newMatrix[row][column] = self[row][column] - secondTerm
        elif isinstance(secondTerm, Matrix):
            if (self.rows == secondTerm.rows) and (self.columns == secondTerm.columns):
                for row in range(self.rows):
                    for column in range(self.columns):
                        if operation == "add":
                            newMatrix[row][column] = self[row][column] + secondTerm[row][column]
                        if operation == "sub":
                            newMatrix[row][column] = self[row][column] - secondTerm[row][column]

        return newMatrix

    def is_square(self):
        return self.rows == self.columns

    def transpose(self):
        newMatrix = Matrix(self.columns, self.rows)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[column][row] = self.matrix[row][column] 

        return newMatrix

    def complement_matrix(self, rowToDelete, columnToDelete):
        newMatrix = deepcopy(self)
        del(newMatrix[rowToDelete])

        for row in range(newMatrix.rows):
            del(newMatrix[row][columnToDelete])

        newMatrix.columns -= 1

        return newMatrix

    def algebric_complement(self, row, column):
        complementMatrix = self.complement_matrix(row, column)
        algebricComplement = (-1)**(row+column) * complementMatrix.determinant()

        return algebricComplement
    def determinant(self):
        if self.is_square():
            if self.rows == 1:
                # If it's a square matrix with only 1 row, it has only 1 element
                det = self[0][0] # The determinant is equal to the element
            elif self.rows == 2:
                det = (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
            else:
                # Laplace's theorem
                det = 0
                for element in range(self.columns):
                    det += self[0][element] * self.algebric_complement(0, element)
            return det
