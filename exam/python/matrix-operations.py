class Matrix:
    def __init__(self, data: list):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def sum(self, otherMatrix):
        if (self.rows!=otherMatrix.rows or self.columns != otherMatrix.columns):
            raise ValueError("The matrices don't have the same quantity of rows so we can't summarize them.")
        newMatrix = []
        for i in range(self.rows):
            newMatrix.append([])
            for j in range(self.columns):
                newMatrix[i].append(self.data[i][j]+otherMatrix.data[i][j])
        return Matrix(newMatrix)
    
    def determinant(self):
        det = 0
        if self.rows != self.columns:
            raise ValueError("Determinant can't be caluclated")
        if self.rows == 2:
            det = self.data[0][0]*self.data[1][1]-self.data[1][0]*self.data[0][1]
        else:
            for i in range(self.columns):
                minor = [[self.data[j][k] for k in range(self.columns) if k!=i] for j in range(1,self.rows)]
                minorMatrix = Matrix(minor)
                sign = (-1)**self.columns
                det+=sign*self.data[0][i]* minorMatrix.determinant()

        return det
    
    def __str__(self):
        result = ""
        for i in range(self.rows):
            result+=" ".join(str(self.data[i][j]) for j in range(self.columns))+"\n"
        return result
                
try:
    matrix1 = [
        [15,4,69, 78],
        [18,18,0],
        [1,63,13],
    ] 
    matrix2 = [
        [15,2,4],
        [18,-23,18],
        [-918,-1,63],
    ]
    newMatrix1 = Matrix(matrix1)
    newMatrix2 = Matrix(matrix2)
    sumMatrix = newMatrix1.sum(newMatrix2)
    print(newMatrix1.determinant())
    print(sumMatrix.__str__())
except ValueError as v:
    print(v)
# print("rows -", newMatrix.rows)
# print(newMatrix.columns)