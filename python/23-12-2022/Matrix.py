import random
import deepcopy
class Matrix:
     def __init__(self, rows, columns):
         self.rows=rows
         self.columns=columns
         self.matrix=[]

         for i in range(rows):
            self.matrix.append([]) # empty rows

        for row in self.matrix:
            for i in range(columns):
                row.append(randint(10)) # Fill the rows with random numbers 

    def add(self, otherMatrix):
        return addorsub(otherMatrix, "add")
    def sub(self, otherMatrix):
        return self.addorsub(otherMatrix, "sub")

    def addorsub(self, matr, operation):
        newMatrix=Matrix(self.rows, self.columns)
        if (self.rows == secondTerm.rows) and (self.columns == secondTerm.columns):
                for row in range(self.rows):
                    for column in range(self.columns):
                        if operation == "add":
                            newMatrix[row][column] = self[row][column] + matr[row][column]
                        elif operation == "sub":
                            newMatrix[row][column] = self[row][column] - matr[row][column]
    
    def get_transpose(self):
        newMatrix= Matrix(self.columns, self.rows)

        for row in range(self.rows):
            for column in range(self.columns):
                newMatrix[column][row]=self.matrix[row][column]

        return newMatrix

    def is_square(self): 
        return self.rows==self.columns

    def complement_matrix(self,rowDel, colDel):
        newMatrix=deepcopy(self)
        del(newMatrix[rowDel])

        for row in range(newMatrix.rows):
            del(newMatrix[row][colDel])
        newMatrix.columns -=1

        return newMatrix
    
    def algebraic_complement(self, row, column):
        complementMatrix=self.complement_matrix(row, column)
        algebraicComplement=(-1)**(row+column) * complementMatrix.get_determinant()
        return algebraicComplement

    def get_determinant(self):
        if self.is_square():
            if self.rows==1:
                det=self[0][0]
            elif self.rows==2:
                det=(self[0][0]*self[1][1])-self[0][1]*self[1][0]
            else:
                #Laplace's theorem
                det=0
                for i in range(self.columns):
                    det+=self[0][i] * self.algebraic_complement(0, i)
            return det
        else:
            raise TypeError("Only square matrix has a determinant.")
   
