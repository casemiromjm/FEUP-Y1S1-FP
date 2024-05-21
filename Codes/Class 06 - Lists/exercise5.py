def mult(M, N):
#check if matrices are compatible (mxn and nxp), so check if columns M == lines N.
#being compatible, should progress to do the mult
#matrix resultant will be mxp
    multipliedMatrix = []
    lines_M = len(M)
    columns_M = len(M[0])
    lines_N = len(N)
    columns_N = len(N[0])

    if lines_N != columns_M:
        return []
    
    for i in range(lines_M):
        row = []
        for j in range(columns_N):
            dotProduct = 0
            for k in range(columns_M):
                dotProduct += M[i][k] * N[k][j]
            row.append(dotProduct)
        multipliedMatrix.append(row)

    return multipliedMatrix