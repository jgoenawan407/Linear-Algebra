from gaussian_elim import gauss_elim
import copy

# to find an inverse with gaussian elimination, we can just use the gauss_elim() function from gaussian_elim, since it will only operate to reduce the base matrix, while also operating on the augmented columns 

m = [[7, 2, -1], [0, 3, -1], [-3, 4, 2]]

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
		if j < 3:
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
