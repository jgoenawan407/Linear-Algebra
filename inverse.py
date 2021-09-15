# Jackson Goenawan, 9/14/21

from gaussian_elim import gauss_elim
import copy

# to find an inverse with gaussian elimination, we can just use the gauss_elim() function from gaussian_elim, since it will only operate to reduce the base matrix, while also operating on the augmented columns 

def inverse(m):

	identity = [([0] * len(m[0])) for i in range(len(m))]

	# filling in identity matrix
	for i in range(len(identity)):
		for j in range(len(identity[0])):

			if i == j:
				identity[i][j] = 1
			else:
				identity[i][j] = 0

	# filling in the augmented matrix
	aug_mat = [([0] * (len(m[0]) * 2)) for i in range(len(m))]

	for i in range(len(aug_mat)):
		for j in range(len(aug_mat[0])):
			if j < len(m):
				aug_mat[i][j] = m[i][j]
			else :
				aug_mat[i][j] = identity[i][j - len(m)]

	print('Matrix: ' + str(m))
	aug_mat = gauss_elim(aug_mat)
	inv_mat = [([0] * len(m[0])) for i in range(len(m))]

	for i in range(len(inv_mat)): 	
		for j in range(len(inv_mat[0])):
			inv_mat[i][j] = aug_mat[i][j + len(m)]

	print('Inverse: ' + str(inv_mat))

m1 = [[1.80, -2.32], [-0.25, 0.60]]
m2 = [[0.3, -0.1, 0.5], [2, 6, 4], [5, 0, 9]]
m3 = [[1, 0, 0], [2, 1, 0], [5, 4, 1]]

inverse(m1)
inverse(m2)
inverse(m3)
