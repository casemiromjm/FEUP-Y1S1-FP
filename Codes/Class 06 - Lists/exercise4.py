def magic(mat):
    matrixDimension = len(mat)
    
#check each line's sum
    for i in range(matrixDimension):
        lineSum = sum(mat[i])
        if lineSum != pastLineSum:
            return False
        pastLineSum = lineSum
    
#check each column's sum
    for i in range(matrixDimension): #column
        tempColumn = []
        for j in range(matrixDimension): #column element of each line
            columnElement = mat[j][i]
            tempColumn.append(columnElement)    
        columnSum = sum(tempColumn)
        if columnSum != pastColumnSum:
            return False
        pastColumnSum = columnSum

#check diagonal sum
    tempDiagonal = []
    for i in range(matrixDimension):
        diagonalElement = mat[i][i]
        tempDiagonal.append(diagonalElement)
    diagonalSum = sum(tempDiagonal)

#check anti diagonal sum
    tempAntiDiagonal = []
    for i in range(matrixDimension):
        antiDiagonalElement = mat[i][(matrixDimension-1) - i]
        tempAntiDiagonal.append(antiDiagonalElement)
    antiDiagonalSum = sum(tempAntiDiagonal)

#check each sum to see if it is the same sum
    if lineSum == columnSum == diagonalSum == antiDiagonalSum:
        return True #magic square
    else:
        return False #not a magic square