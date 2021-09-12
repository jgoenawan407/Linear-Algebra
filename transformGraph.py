import matplotlib.pyplot as plt
from matrix_arithmetic import mult

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Graph')

def transform(trans_mat, init_pts):

  if len(trans_mat) != 2 and len(trans_mat[0]) != 2 and len(init_pts) != 2:
    return('Improper input dimensions')

  plt.plot(init_pts[0], init_pts[1],'o') # requires input to be a 2D array of length 2
  transformed = mult(trans_mat, init_pts)
  plt.plot(transformed[0], transformed[1], 'o') 
  plt.show()

m = [[2, 0], [0, 2]] # transformation matrix
v = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]] # x-coords in first array, y-coords in 2nd
transform(m, v)