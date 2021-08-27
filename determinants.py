# Jackson Goenawan, 8/26/21

import copy

def det(m): # recursively runs determinant process until you get to a 2x2

  if len(m) != len(m[0]):
    return("Matrix is not square")

  if len(m) == 2:
    return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])

  det_sum = 0

  for i in range(len(m)):
    
    # matrix excluding the row and column we're currently "covering"  
    m_p = [row[: i] + row[i + 1:] for row in (m[: 0] + m[1:])] # must include m[: 0] term or else it just doesn't count anything for the sub matrix
    sign = (-1) ** i # accounts for sign pattern
    det_sum += sign * m[0][i] * det(m_p)

  return det_sum

def cramer_solve(coeff, constants):
	
	d = det(coeff) # determinant of coefficient matrix

	if d == 0:
		return("System is linearly independent")

	solns = [[0] for i in range(len(coeff))]

	for i in range(len(coeff)):

		m_i = copy.deepcopy(coeff)

		for j in range(len(coeff[0])):

			m_i[j][i] = constants[j][0]
		solns[i] = det(m_i) / d
	return(solns)

m1 = [[1, 2, 3], [4, 5, 6]] # returns error
m2 = [[0, 4, -1, 5], [-4, 0, 3, 2], [1, -3, 0, 1], [-5, 2, -1, 0]]
m3 = [[4, 7, 0, 0], [2, 8, 0, 0], [0, 0, 1, 5],[0, 0, -2, 2]]
diag = [[4, -1, 8], [0, 2, 3], [0, 0, 5]]

print('Matrix 1: ' + str(m1))
print('Matrix 2: ' + str(m2))
print('Matrix 3: ' + str(m3))
print('Diagonal Matrix: ' + str(diag))

print('Determinant of Matrix 1: ' + str(det(m1)))
print('Determinant of Matrix 1: ' + str(det(m2)))
print('Determinant of Matrix 1: ' + str(det(m3)))
print('Determinant of Matrix 1: ' + str(det(diag)))

# solving system with cramer's rule
coeff = [[3, -5], [6, 16]] # matrix holding variable coefficients
constants = [[15.5], [5.0]] # constants (on right side of =)
print('Cramer Solution: ' + str(cramer_solve(coeff, constants)))
