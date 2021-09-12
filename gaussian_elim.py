# Jackson G, Robbie G, 9/11/21

import copy

def rowSwap(M,r1,r2):
    matrix = copy.deepcopy(M)
    matrix[r1] = M[r2]
    matrix[r2] = M[r1]
    return(matrix)

def rowScale(M,r1,s):
    matrix = copy.deepcopy(M)
    for i in range(len(M[r1])):
        matrix[r1][i] = M[r1][i] * s
    return(matrix)

def rowSum(M,r1,r2,s):
    matrix = copy.deepcopy(M)
    for i in range(len(M[r1])):
        matrix[r2][i] = (M[r1][i] * s) + M[r2][i]
    return(matrix)

def gauss_elim(M):
    
    matrix = copy.deepcopy(M)
    
    last = len(matrix)
    all_zero = True
    
    for i in range(last):
        
        row_zero = True
        
        for j in range(len(matrix[0])):
            
            if matrix[i][j] != 0:
                row_zero = False
                all_zero = False
                break
        
        if row_zero:
            matrix = rowSwap(matrix, i, last - 1) # moves the all-zero rows to the bottom (rref convention)
            last -= 1
    
    if all_zero:
        return matrix # matrix is all zero, already reduced
    
    r = 1
    while (matrix[0][0] == 0): # keep going until this pivot is switched successfully
       
       matrix = rowSwap(matrix, 0, i)
       r += 1
   
    matrix = rowScale(matrix, 0, 1 / matrix[0][0]) # getting M[0][0] to be 1
    pivots = min(len(matrix), len(matrix[0])) #  num of pivots will be the lesser of the number of rows or number of columns - 1
    
    for r in range(pivots): # going through columns
        
        for i in range(pivots): # going through rows
            
            if (i == r):
                 continue # skips main diagonal elements, or else they will all be 0
            
            if (matrix[r][r] != 0):
                matrix = rowSum(matrix, r, i, (matrix[i][r] * -1)/(matrix[r][r])) # adding to the row the values that make [i][r] = 0
    
    for i in range(pivots):
        
        if matrix[i][i] != 0:
            matrix = rowScale(matrix, i, 1 / matrix[i][i]) # scaling all diagonal elements to be 1

    return matrix

m1 = [[4, -6, -11], [-3, 8, 10]]
m2 = [[0, 8, 6, -6], [1, 1, -1, 9], [-2, 4, -6, 40]]
m3 = [[3, -0.5, 0.6], [1.5, 4.5, 6.0]]

print(gauss_elim(m1))
print(gauss_elim(m2))
print(gauss_elim(m3))
